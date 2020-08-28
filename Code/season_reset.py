# Complete and working rank resetter

import os

directory = os.path.dirname(os.path.abspath('rank_problems.py'))

print('ARE YOU SURE YOU WANT TO RESET RANKS? (y/n)')
if input().lower().strip() == 'y':
    for div in ['alg1', 'geo', 'alg2', 'precal', 'calc']:
        open(directory+'/Student_T_Scores/'+div+'.txt', 'w').close()
