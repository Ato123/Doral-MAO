
import os
from math import sqrt

directory = os.path.dirname(os.path.abspath('anti_cheat.py'))

print('format for divisions: alg1, geo, alg2, precal, calc, stats')
print('What division is being scanned right now?')
div = input()

print('How much T-score gain do you consider cheating?')
dif = float(input())

recent = open(directory+'/Student_Rankings_Recent/'+div+'.txt', 'r')

mean = 0
size = 0

name_score = dict()

for line in recent:
    spl = line.split(' ')
    name = spl[1]+' '+spl[2]
    score = int(spl[3])

    mean += score
    size += 1

    name_score[name] = score

mean /= size

sigma = 0

for score in name_score.values():
    sigma += (score-mean)**2
sigma = sqrt(sigma/size)
if sigma == 0:
    sigma = 1

overall = open(directory+'/Student_Rankings_Total/'+div+'.txt', 'r')

name_tscore = dict()

for line in overall:
    spl = line.split(' ')
    name = spl[1]+' '+spl[2]
    tscore = float(spl[3])

    name_tscore[name] = tscore

cheaters = open(directory+'/Cheaters/'+div+'.txt', 'w')
cheaters.write('Difference Threshold: '+str(dif)+'\n')
for name in name_score.keys():
    if name in name_tscore.keys():
        tscore = (name_score[name]-mean)/sigma
        tscore = 10*tscore+50

        if tscore - name_tscore[name] >= dif:
            cheaters.write(name+' - overall: '+str(name_tscore[name])+' - last test: ' + str(tscore)+'\n')

cheaters.close()
