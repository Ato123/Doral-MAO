# Complete and working submission maker

import os
import glob


directory = os.path.dirname(os.path.abspath('enter_submissions.py'))

print('format for divisions: alg1, geo, alg2, precal, calc, stats')
print('What division is being recorded right now?')
div = input()

print('Clear previous submissions? (y/n)')
if input().lower().strip() == 'y':
    for f in glob.glob(directory+'/Moodle_Submissions/'+div+'/*'):
        os.remove(f)

print('names should be inputted in first-name last-name order')
print('Inputted answers must be in a single line with blank answers being marked as x')
print('\nexample input:')
print('alberto alvarez calc\nabcadacebcacaaebcaebbeacadbdca')

print('type exit to stop the program')

while True:
    print('Name?')
    name = input().lower().strip()
    if name == 'exit':
        break
    file = open(directory+'/Moodle_Submissions/'+div+'/'+name+'.txt', 'w')
    print('Answers?')
    file.write(input().lower().strip())
    file.close()
