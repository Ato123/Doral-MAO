# Complete and working problem ranker

import os
import glob

directory = os.path.dirname(os.path.abspath('rank_problems.py'))

print('format for divisions: alg1, geo, alg2, precal, calc, stats')
print('What division is being ranked right now?')
div = input()

print('Clear previous submissions? (y/n)')
if input().lower().strip() == 'y':
    open(directory+'/Problem_Rankings/'+div+'.txt', 'w').close()

file = open(directory+'/Problem_Rankings/'+div+'.txt', 'w')

score = [0]*30

scoring = {'r': 5, 'b': 1, 'w': 0}

for sub in glob.glob(directory+'/Graded_Submissions/'+div+'/*'):
    s = open(sub)
    s.readline()
    ans = s.readline()
    for i in range(30):
        score[i] += scoring[ans[i]]

tosort = sorted(score.copy())
aux = score.copy()
ranked = [0]*30

for i in range(30):
    ind = aux.index(tosort[i])
    ranked[i] = ind+1
    aux[ind] = -1

rankval = [0]*30
rankval[0] = 1

for i in range(1, 30):
    if ranked[i] == ranked[i-1]:
        rankval[i] = rankval[i-1]
    else:
        rankval[i] = i+1

for i in range(0, 30):
    file.write(str(rankval[i])+' '+str(ranked[i])+'\n')

file.close()
