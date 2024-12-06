#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 10:12:43 2024

@author: stephanchang
"""
import numpy as np
pi = np.pi
import matplotlib.pyplot as plt

L=1024

signal = np.sin(np.arange(0,100*pi,100*pi/L))
signal = np.tile(signal,[100,1])
noise = np.random.rand(100,L)/10-0.05
plt.figure()
plt.plot(signal[0]+noise[0])
plt.title('original signal')
plt.show()

fs = np.fft.fft((noise+signal),axis = 1)/L
plt.figure()
plt.plot(np.abs(fs[0]))
plt.title('fft signal')
plt.show()

signal_ifft = np.fft.ifft(fs,axis = 1)*L
plt.figure()
plt.plot(signal_ifft[0].real)
plt.title('ifft signal')
plt.show()


ratios_std = np.zeros(6)
ratios_signal = np.zeros(6)
for ii, L in enumerate([256,512,1024,1560,2048,4096]):
    signal = np.sin(np.arange(0,100*pi,100*pi/L))
    signal = np.tile(signal,[100,1])
    noise = np.random.rand(100,L)/10-0.05
    std1=np.std(noise,0)
    
    fs = np.fft.fft((noise+signal),axis = 1)/L
    
    peak = np.max(np.abs(fs[0]))
    ratios_signal[ii] = peak
    fs[np.abs(fs)>0.1]=0
    
    std2=np.std(np.abs(fs),0)
    ratio = np.mean(std2)/np.mean(std1)
    ratios_std[ii] = ratio

plt.figure()
plt.plot([256,512,1024,1560,2048,4096],ratios_std)
plt.title('noise ratio freq/time ')
plt.show()
print('FFT does averaging, so noise decrease in the scale of sqrt(Length)')
plt.figure()
plt.plot([256,512,1024,1560,2048,4096],ratios_signal)
plt.title('signal level in freq')
plt.show()


