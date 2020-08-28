import os
import glob

directory = os.path.dirname(os.path.abspath('rank_problems.py'))

print('format for divisions: alg1, geo, alg2, precal, calc')
print('What division is being ranked right now?')
div = input()

print('Clear previous submissions? (y/n)')
if input().lower().strip() == 'y':
    open(directory+'/Student_Rankings_Recent/'+div+'.txt', 'w').close()

file = open(directory+'/Student_Rankings_Recent/'+div+'.txt', 'w')

mapped = dict()
scores = []

size = 0

for graded in glob.glob(directory+'/Graded_Submissions/'+div+'/*'):
    score = int(open(graded).readline())
    name = graded[graded.rindex('/')+1:-4]

    scores.append(score)

    if score not in mapped.keys():
        mapped[score] = []
    mapped[score].append(name)

    size += 1

tosort = sorted(scores.copy())

ranked = []
rankedval = [0]*size
ind = 0

for i in range(len(scores)):
    score = tosort[i]
    ranked.extend(mapped[score])

    for j in range(ind, len(ranked)):
        rankedval[j] = ind+1
    ind = len(ranked)

for i in range(size):
    file.write(str(rankedval[i])+' '+ranked[i]+'\n')

file.close()
