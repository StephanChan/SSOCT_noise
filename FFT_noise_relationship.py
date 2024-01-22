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

data = np.sin(np.arange(0,100*pi,100*pi/L))
data = np.tile(data,[1000,1])

noise = np.random.rand(data.shape[0],L)*0.2

std1=np.std(noise,0)

# plt.figure()
# data = data + noise
# for ii in range(0,1000,10):
#     plt.plot(data[ii,:])
# plt.title('original data')

# plt.figure()
# plt.plot(std1)
# plt.title('std before fft')

fs = np.fft.fft((data+noise),axis = 1)/L
std2=np.std(np.abs(fs),0)
m = np.mean(np.abs(fs),0)

print('noise ratio before and after fft: ', np.mean(std1)/np.mean(std2))

# plt.figure()
# plt.plot(m)
# plt.title('mean after fft')

# plt.figure()
# plt.plot(std2)
# plt.title('std after fft')



