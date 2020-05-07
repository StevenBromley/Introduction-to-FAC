import sys
from pfac.crm import *
import os
kronos_dir = '/home/steve/FAC_dir/kronos/Kronos_v3.1'
ReadKronos(kronos_dir, 10, 1, 'Ne', 'H2', '',)

AddIon(2, 0, 'Ne8b')
SetBlocks(2.0)
SetCxtDist(1, 50, 10, 40, 60)
SetTRRates(0)
SetCXRates(10, 'H2')
SetCxtDensity(2e-3) #gives neutral  density of ~2E-7 cm^-3. Assumed P_ebit = 1E-9 mbar
InitBlocks()
SetIteration(1e-05, 0.5)
LevelPopulation()
SpecTable('Ne8b.sp')
PrintTable('Ne8b.sp', 'Ne8.sp')
SelectLines('Ne8b.sp', 'Ne8.ln', 2, 0, 0, 1e10)