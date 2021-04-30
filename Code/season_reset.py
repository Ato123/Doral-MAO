# Complete and working archiver, which also resets everything
# Verified as of 4/29/2021

import os
import shutil


def reset_txts(direc):
    for div in ['alg1', 'geo', 'alg2', 'precal', 'calc', 'stats']:
        open(direc+div+'.txt', 'w').close()


directory = os.path.dirname(os.path.abspath('rank_problems.py'))

print('Are you sure you want to reset the leaderboard? Student T-scores and overall rankings will be archived. (y/n)')
if input().lower().strip() == 'y':

    archive = input('\nName of archive?')
    archive = directory+'/Archive/'+archive
    os.mkdir(archive)

    os.mkdir(archive+'/Student_T_Scores')
    os.mkdir(archive + '/Student_Rankings_Total')

    for div in ['alg1', 'geo', 'alg2', 'precal', 'calc', 'stats']:
        with open(directory+'/Student_T_Scores/'+div+'.txt', 'r') as copy, open(archive+'/Student_T_Scores/'+div+'.txt', 'w') as paste:
            paste.write(copy.read())

    for div in ['alg1', 'geo', 'alg2', 'precal', 'calc', 'stats']:
        with open(directory+'/Student_Rankings_Total/'+div+'.txt', 'r') as copy, open(archive+'/Student_Rankings_Total/'+div+'.txt', 'w') as paste:
            paste.write(copy.read())

    for file in ['Cheaters', 'Problem_Rankings', 'Student_Rankings_Recent', 'Student_Rankings_Total', 'Student_T_Scores', 'Test_Answers']:
        reset_txts(directory+'/'+file+'/')

    for file in ['Graded_Submissions', 'Student_Submissions']:
        for div in ['alg1', 'geo', 'alg2', 'precal', 'calc', 'stats']:
            fdir = directory+'/'+file+'/'+div
            shutil.rmtree(fdir)
            os.mkdir(fdir)

    with open(directory + '/TEMPLATE.md', 'r') as copy, open(directory[:-4] + 'README.md', 'w') as paste:
        paste.write(copy.read())

    with open(directory + '/TEMPLATE.md', 'r') as copy, open(directory + '/README.md', 'w') as paste:
        paste.write(copy.read())
