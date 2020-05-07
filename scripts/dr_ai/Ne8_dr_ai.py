import sys
from pfac.fac import *
import os
import time
import numpy as np

start = time.time()
SetAtom('Ne')
#Ne8+
Config('1*2', group = '8_1l')
Config('2*2', group = '8_2l')
Config('1*1 2*1', group = '8_1l2l')
Config('1*1 3*1', group = '8_1l3l')
Config('1*1 4*1', group = '8_1l4l')
Config('2*1 3*1', group = '8_2l3l')
Config('2*1 4*1', group = '8_2l4l')
ne8 = ['8_1l','8_2l', '8_1l2l', '8_1l3l', '8_1l4l', '8_2l3l', '8_2l4l']
ConfigEnergy(0)
OptimizeRadial(['8_1l'])
ConfigEnergy(1)
Structure('Ne8b.en',ne8)
#Ne9+
Config('1*1', group = '1s')
Config('2*1', group = '2l')
Config('3*1', group = '3l')
Config('4*1', group = '4l')
Config('5*1', group = '5l')
Config('6*1', group = '6l')
Config('7*1', group = '7l')
Config('8*1', group = '8l')
#Ne10
Config('' , group= 'ne10ground')
ne9 = ['1s','2l', '3l', '4l', '5l', '6l', '7l', '8l']
ne10 = ['ne10ground']
ConfigEnergy(0)
OptimizeRadial(['1s'])
ConfigEnergy(1)
Structure('Ne8b.en', ne9)
Structure('Ne8b.en', ne10)
MemENTable('Ne8b.en')
PrintTable('Ne8b.en', 'Ne8.en', 1)
TransitionTable('Ne8b.tr', ne8, ne8)
PrintTable('Ne8b.tr', 'Ne8.tr', 1)
print('Structure Complete. Elapsed Time: {:} seconds'.format(time.time() - start))

#DR/AI:
drai = time.time()
print('Starting DR and AI...')
AITable('Ne8b.ai', '8_2l', '1s')
AITable('Ne8b.ai', '8_2l3l', '1s')
AITable('Ne8b.ai', '8_2l4l', '1s')
PrintTable('Ne8b.ai', 'Ne8.ai', 1)
print('AI Finished. Total Elapsed Time: {:} seconds'.format(time.time() - drai))

