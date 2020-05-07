import sys
from pfac.fac import *
import os
import time
import numpy as np

start = time.time()
SetAtom('Ne')
Config('1*2', group = '1l2')
Config('2*2', group = '2l2')
Config('1*1 2*1', group = '1l2l')
Config('1*1 3*1', group = '1l3l')
Config('1*1 4*1', group = '1l4l')
Config('1*1 5*1', group = '1l5l')
Config('1*1 6*1', group = '1l6l')
Config('1*1 7*1', group = '1l7l')
Config('1*1 8*1', group = '1l8l')
Config('2*1 3*1', group = '2l3l')
Config('2*1 4*1', group = '2l4l')
ne8 = ['1l2', '2l2', '1l2l', '1l3l', '1l4l', '1l5l', '1l6l', '1l7l', '1l8l', '2l3l', '2l4l']
#Ne9 ground:
Config('1*1', group = '1l')
ne9 = ['1l']
ConfigEnergy(0)
OptimizeRadial(['1l2'])
ConfigEnergy(1)
Structure('Ne8b.en',ne8)
Structure('Ne8b.en',ne9)

MemENTable('Ne8b.en')
PrintTable('Ne8b.en', 'Ne8.en', 1)
TransitionTable('Ne8b.tr', ne8, ne8)
PrintTable('Ne8b.tr', 'Ne8.tr', 1)
#Start EIE:
eie = time.time()
CETable('Ne8b.ce', ne8, ne8)
PrintTable('Ne8b.ce', 'Ne8.ce',1)
print('EIE Finished. Elapsed time: {:}'.format(time.time()-eie))


