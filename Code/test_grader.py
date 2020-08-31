# Complete and working test grader

import os
import glob

print('MAKE SURE ANSWER FILES ARE UPDATED WITH THE RIGHT ANSWERS!!!')

directory = os.path.dirname(os.path.abspath('test_grader.py'))

print('format for divisions: alg1, geo, alg2, precal, calc, stats')
print('What division is currently being graded?')
div = input()

print('Clear previous submissions? (y/n)')
if input().lower().strip() == 'y':
    for f in glob.glob(directory+'/Graded_Submissions/'+div+'/*'):
        os.remove(f)

ans = open(directory+'/Test_Answers/'+div+'.txt').readline()

print('Grading...')

for f in glob.glob(directory+'/Moodle_Submissions/'+div+'/*'):
    sub = open(f).readline()
    filename = f[f.rindex('/')+1:]

    print('grading', filename)

    graded = open(directory+'/Graded_Submissions/'+div+'/'+filename, 'w')

    score = 0
    checked = ''
    for i in range(30):
        if sub[i] == ans[i]:
            score += 5
            checked += 'r'
        elif sub[i] == 'x':
            score += 1
            checked += 'b'
        else:
            checked += 'w'
    graded.write(str(score))
    graded.write('\n'+checked)

    print(score)

    graded.close()

print('Done!')
