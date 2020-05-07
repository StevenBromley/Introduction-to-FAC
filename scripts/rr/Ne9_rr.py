import sys
from pfac.fac import *
import os
import time
import numpy as np

start = time.time()
SetAtom('Ne')
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
Structure('Ne9b.en', ne9)
Structure('Ne9b.en', ne10)
MemENTable('Ne9b.en')
PrintTable('Ne9b.en', 'Ne9.en', 1)
TransitionTable('Ne9b.tr', ne9, ne9)
PrintTable('Ne9b.tr', 'Ne9.tr', 1)
print('Structure Complete. Elapsed Time: {:} seconds'.format(time.time() - start))

#RR:
rr_start = time.time()
print('Starting RR...')
RRTable('Ne9b.rr', ne9, ne10)
PrintTable('Ne9b.rr', 'Ne9.rr', 1)
print('RR Finished. Elapsed Time: {:} seconds'.format(time.time() - rr_start))
