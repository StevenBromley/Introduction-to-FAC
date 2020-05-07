import sys
from pfac.crm import *
import os

AddIon(2, 1.0, 'Ne8b')
SetBlocks()
SetTRRates(0)

SetCERates(1) #1 includes collisional de-excitation
e_cen = 1000
e_min = e_cen - 300
e_max = e_cen + 300
SetEleDist(1,e_cen,40,e_min,e_max)
SetEleDensity(1e2) #in units of 10^10 per cm^3

InitBlocks()
SetIteration(1e-05, 0.5)
LevelPopulation()

SpecTable('Ne8b.sp')
PrintTable('Ne8b.sp', 'Ne8.sp')
SelectLines('Ne8b.sp', 'Ne8_eie.ln', 2, 0, 0, 1e10)