# Complete and working ranking systems for the entire season
# Verified as of 4/29/2021

import os

directory = os.path.dirname(os.path.abspath('rank_students_overall.py'))

print('format for divisions: alg1, geo, alg2, precal, calc, stats')
print('What division is being ranked right now?')
div = input()

print('\nClear previous rankings for this division? (y/n)')
if input().lower().strip() == 'y':
    open(directory + '/Student_Rankings_Total/' + div + '.txt', 'w').close()

file = open(directory + '/Student_Rankings_Total/' + div + '.txt', 'w')

name_score = dict()
mapped = dict()
scores = []

size = 0

for line in open(directory+'/Student_T_Scores/'+div+'.txt'):
    spl = line.split(' ')
    name = spl[0]+' '+spl[1]
    score = float(spl[2])

    name_score[name] = score
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
    file.write(str(rankedval[i])+' '+ranked[i]+' '+str(name_score[ranked[i]])+'\n')

file.close()
