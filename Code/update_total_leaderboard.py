
import os

directory = os.path.dirname(os.path.abspath('update_total_leaderboard.py'))

print('format for divisions: alg1, geo, alg2, precal, calc, stats')
print('What division is being posted right now?')
div = input()

readme = open(directory+'/README.md')
lines = [line for line in readme]
readme.close()

full = {'alg1':'Algebra 1', 'geo':'Geometry', 'alg2':'Algebra 2', 'precal':'Precalculus', 'calc':'Calculus', 'stats':'Statistics'}
abbr = ['alg1', 'geo', 'alg2', 'precal', 'calc', 'stats']

idiv = -1
for i in range(len(abbr)):
    if abbr[i] == div:
        idiv = i

sind = -1
for i in range(len(lines)-1, -1, -1):
    if full[div] in lines[i]:
        sind = i

eind = -1
if idiv != len(abbr)-1:
    for i in range(len(lines)-1, -1, -1):
        if full[abbr[idiv+1]] in lines[i]:
            eind = i
if eind == -1:
    for i in range(len(lines)-1,-1,-1):
        if '___' in lines[i]:
            eind = i
    eind -= 1

del lines[sind+1:eind-1]

count = 0
for line in open(directory+'/Student_Rankings_Total/'+div+'.txt'):
    spl = line.split(' ')
    lines.insert(sind+1, f'\n<b>{spl[0]} -</b> {spl[1][0].upper()+spl[1][1:].lower()} {spl[2][0].upper()+spl[2][1:].lower()}: {spl[3]}\n</br>\n')
    sind += 1
    count += 1
if count == 0:
    lines.insert(sind+1, '\nNone\n</br>\n')

open(directory+'/README.md', 'w').close()
write = open(directory+'/README.md', 'w')
write.writelines(lines)
write.close()

with open(directory+'/README.md', 'r') as copy, open(directory[:-4]+'README.md', 'w') as paste:
    paste.write(copy.read())
