# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 19:42:42 2025

@author: shuai
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:22:23 2024

@author: stephanchang
"""
import numpy as np

########################### 
# print('Knowing Camera readout noise and electron well depth, calculating measured noise using a specific camera...\n')

# input detector info
readout_noise = 30 # number of electrons
electron_well_depth = 20000 # number of electrons

Num_pixels = 1024


system_noise_time_domain = readout_noise + np.sqrt(electron_well_depth) # read out noise + shot noise

if readout_noise < np.sqrt(electron_well_depth)/10:
    print('system is shot noise limited\n')
elif readout_noise < np.sqrt(electron_well_depth):
    print('system is almost shot noise limited\n')
else:
    print('system is not shot noise limited')

print('the time domain noise measured by this camera will be :',round(system_noise_time_domain,3),' electrons\n')

system_noise_freq = system_noise_time_domain/np.sqrt(Num_pixels)/2.155
print('the freq domain noise is:',round(system_noise_freq,3),' electrons\n')
print('\n\n\n')

SNR = 20*np.log10(electron_well_depth/system_noise_freq)
print('the theoretical SNR of this system is: ', round(SNR,3), ' dB, note this is assuming a rectangular spectrum, a gaussian spectrum will have slightly less SNR')






