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
Structure('Neb.en', ne9)
Structure('Neb.en', ne10)
MemENTable('Neb.en')
PrintTable('Neb.en', 'Ne.en', 1)
TransitionTable('Neb.tr', ne9, ne9)
PrintTable('Neb.tr', 'Ne.tr', 1)
print('Structure Complete. Elapsed Time: {:} seconds'.format(time.time() - start))

#EIE:
eie1 = time.time()
print('Starting EII...')
#
CETable('Ne9b.ce', ne9, ne9)
PrintTable('Ne9b.ce', 'Ne9.ce', 1)
print('EIE Ne9 -> Ne9 finished. Time: {:} s'.format(time.time() - eie1))

