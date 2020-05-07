import matplotlib.pyplot as plt
import numpy as np
from brokenaxes import brokenaxes
def gaussian(x, *p):
    A, mu, sigma = p
    return A*np.exp(-(x-mu)**2/(2*sigma**2))

def spec_convolve(x, t_arr,res):
    gauss_tot = np.zeros((len(x_range[:]),1))
    for i in range(0,len(t_arr[:,0])):
        A_0 = t_arr[i,6]
        mu_0 = t_arr[i,4]
        sigma_0 = res/ 2
        p0 = [A_0,mu_0,sigma_0] #C_0]           
        g1 = gaussian(x, *p0)
        for j in range(0,len(g1[:])):       
            gauss_tot[j] = gauss_tot[j] + g1[j]

    return(gauss_tot)
#%% load data
trans2 = np.genfromtxt('Ne8_eie.ln')
trans6 = np.genfromtxt('Ne8.ln')
resolution = 6 # spectrometer resolution in [ev]; used to convolve
#%%
glob_min = 10000
glob_max = 0
x_min = np.amin(trans2[:,4]) / 2
x_min2 = np.amin(trans6[:,6]) /2
x_max = np.amax(trans2[:,4]) + 50
x_max2 = np.amax(trans6[:,6]) + 50
if (x_min < x_min2):
    glob_min = x_min
else:
    glob_min = x_min2
    
if (x_max < x_max2):
    glob_max = x_max2
else:
    glob_max = x_max

x_range = np.linspace(glob_min,glob_max,10000)
t2 = spec_convolve(x_range,trans2, resolution)
t6 = spec_convolve(x_range,trans6, resolution)
#%%
plt.clf()
plt.figure(figsize = (10,5))
plt.rcParams.update({'font.size': 12})

ne_max = np.amax(t2[:])
ne_rmax = np.amax(trans2[:,6])
ne2_max = np.amax(t6[:])
ne2_rmax = np.amax(trans6[:,6])

plt.plot(x_range, t2 / ne_max , color = 'black', linestyle = '-', label = 'Ne8+ EIE Spectra')
plt.plot(x_range, t6 / ne2_max, color = 'red', linestyle = '-', label = 'Ne8+ CX Spectra')

for i in range(0,len(trans2[:,0])):
    plt.axvline(trans2[i,4], ymin = 0, ymax = trans2[i,6] / ne_rmax, color = 'k', linestyle = '--')
for i in range(0,len(trans6[:,0])):
    plt.axvline(trans6[i,4], ymin = 0, ymax = trans6[i,6] / ne2_rmax, color = 'red', linestyle = '-')
     
plt.ylim(0,1)
plt.legend()
plt.xlabel('Energy [eV]')
plt.ylabel('Intensity (arb. units)')
plt.grid(True)
plt.tight_layout()
plt.savefig('CX_EIE_comp.pdf')