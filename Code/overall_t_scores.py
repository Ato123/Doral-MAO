# Complete and working T-score calculator

import os
import glob
from math import sqrt

directory = os.path.dirname(os.path.abspath('overall_t_scores.py'))

print('format for divisions: alg1, geo, alg2, precal, calc')
print('What division is being calculated right now?')
div = input()

# Calculate T scores
scoremap = dict()
size = 0
sum = 0

for grade in glob.glob(directory+'/Graded_Submissions/'+div+'/*'):
    score = int(open(grade).readline())
    name = grade[grade.rindex('/') + 1:-4]

    scoremap[name] = score
    size += 1
    sum += score

mean = sum/size
sigma = 0
for score in scoremap.values():
    sigma += (mean - score)**2

sigma /= size
sigma = sqrt(sigma)

tscore = dict()
for name in scoremap.keys():
    z = (scoremap[name]-mean)/sigma
    t = 10*z+50
    tscore[name] = t

current = open(directory+'/Student_T_Scores/'+div+'.txt', 'r')

currscoremap = dict()
currfreqmap = dict()

for line in current:
    info = line.split(' ')
    name = info[0]+' '+info[1]
    t = float(info[2])
    freq = int(info[3])

    currscoremap[name] = t
    currfreqmap[name] = freq

for name in tscore.keys():
    if name not in currscoremap.keys():
        currscoremap[name] = 0
        currfreqmap[name] = 0

    currscoremap[name] = currscoremap[name]*currfreqmap[name]+tscore[name]
    currfreqmap[name] += 1
    currscoremap[name] = currscoremap[name]/currfreqmap[name]

open(directory+'/Student_T_Scores/'+div+'.txt', 'w').close()
current = open(directory+'/Student_T_Scores/'+div+'.txt', 'w')
for name in currscoremap.keys():
    current.write(name+' '+str(currscoremap[name])+' '+str(currfreqmap[name])+'\n')

current.close()
