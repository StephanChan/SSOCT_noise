#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:22:23 2024

@author: stephanchang
"""
import numpy as np

########################### 
print('Knowing detector NEP, calculating measured noise using a specific digitizer...\n')

# input detector info
detector_NEP = 2.5 # pW/Hz^0.5
detector_gain = 156/2 # uW/V
# input digitizer info
freq = 500e6 # Hz
digitizer_range = 0.4 # V

Num_samples = 2560


system_noise_time = detector_NEP * 1e-12 * np.sqrt(freq) / (detector_gain * 1e-6) / digitizer_range

print('the time domain detector noise measured by this digitizer will be :',round(system_noise_time,5),' of digitizer dynamic range\n')

system_noise_freq = system_noise_time/np.sqrt(Num_samples)/2.155
print('the freq domain detector noise normalzed by digitizer dynamic range will be :',round(system_noise_freq,7))
print('\n\n\n')
#############################
print('Knowing measured detector noise using a specific digitizer, calculating NEP...\n')

# input detector info
measured_noise = 1/4096 # time domain standard deviation of digitizer range
detector_gain = 156/2 # uW/V
# input digitizer info
freq = 250e6 # Hz
digitizer_range = 2 # V

Num_samples = 1024

NEP = measured_noise * digitizer_range * detector_gain *1e-6/ np.sqrt(freq)*1e12

print('the detector NEP will be :', round(NEP,3),'pW/Hz^0.5')
print('\n\n\n')
###############################
print('calculating theoretical OCT SNR...\n')
sample_arm_power = 1 # mW
ref_arm_power = 1 # mW
detector_NEP = 2.5 # pW/Hz^0.5
freq = 250e6 # Hz
wavelength = 1064 # nm
c = 3e8 # m/s
planck_constant = 6.626e-34 # J*s
Num_samples = 1280

SNR = np.sqrt(2*sample_arm_power*1e-3*ref_arm_power*1e-3)/np.sqrt(\
      pow(detector_NEP*1e-12,2)*freq +
      2*ref_arm_power*1e-3*planck_constant*c/(wavelength*1e-9)*freq\
          )*np.sqrt(Num_samples)*2.155
    
print('Theoretical SNR will be :', round(20*np.log10(SNR),1),' dB\n')

ratio = np.sqrt(\
      pow(detector_NEP*1e-12,2) +
      2*ref_arm_power*1e-3*planck_constant*c/(wavelength*1e-9)\
          )\
    /\
        np.sqrt(2*ref_arm_power*1e-3*planck_constant*c/(wavelength*1e-9))
print('The ratio of total noise and shot noise is :', round(ratio,2),'\n')

if ratio<1.5:
    print('system is almost shot noise limited\n')
else:
    print('system is not shot noise limited')






