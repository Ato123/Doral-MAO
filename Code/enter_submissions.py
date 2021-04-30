# Complete and working submission maker
# Verified as of 4/29/2021

import os
import glob


directory = os.path.dirname(os.path.abspath('enter_submissions.py'))

print('format for divisions: alg1, geo, alg2, precal, calc, stats')
print('What division is being recorded right now?')
div = input()

print('\nClear previous submissions for this division? (y/n)')
if input().lower().strip() == 'y':
    for f in glob.glob(directory+'/Student_Submissions/'+div+'/*'):
        os.remove(f)

print('\nnames should be inputted in first-name last-name (Capital letters included)')
print('Inputted answers must be in a single line with blank answers being marked as x')
print('\nexample input:')
print('alberto alvarez\nabcdexabcdexabcdexabcdexabcdex')

print('type exit to stop the program')

while True:
    print()
    name = input().lower().strip()
    if name == 'exit':
        break
    file = open(directory+'/Student_Submissions/'+div+'/'+name+'.txt', 'w')

    file.write(input().lower().strip())
    file.close()
