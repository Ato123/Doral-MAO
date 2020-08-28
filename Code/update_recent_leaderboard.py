import os

directory = os.path.dirname(os.path.abspath('rank_students_overall.py'))

print('format for divisions: alg1, geo, alg2, precal, calc')
print('What division is being posted right now?')
div = input()

readme = open(directory+'/README.md')
lines = [line for line in readme]
readme.close()

full = {'alg1':'Algebra 1', 'geo':'Geometry', 'alg2':'Algebra 2', 'precal':'Precalculus', 'calc':'Calculus'}
abbr = ['alg1','geo', 'alg2', 'precal', 'calc']

idiv = -1
for i in range(len(abbr)):
    if abbr[i] == div:
        idiv = i

sind = -1
for i in range(len(lines)):
    if full[div] in lines[i]:
        sind = i

eind = -1
if idiv != len(abbr)-1:
    for i in range(len(lines)):
        if full[abbr[idiv+1]] in lines[i]:
            eind = i
if eind == -1:
    for i in range(len(lines)):
        if 'Last Practice' in lines[i]:
            eind = i

del lines[sind+1:eind]

for line in open(directory+'/Student_Rankings_Recent/'+div+'.txt'):
    spl = line.split(' ')
    lines.insert(sind+1, f'\n<font size="+=2">{spl[0]}</font> <b>{spl[1]} {spl[2]}</b> {spl[3]}')
    sind += 1

open(directory+'/README.md', 'w').close()
write = open(directory+'/README.md', 'w')
write.writelines(lines)
write.close()

with open(directory+'/README.md', 'r') as copy, open(directory[:-4]+'README.md', 'w') as paste:
    paste.write(copy.read())
