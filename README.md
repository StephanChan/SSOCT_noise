# SSOCT_noise
noise and SNR analysis of swept source OCT that use a balanced detector and digitizer for readout

Different balanced detector can have different gains, some output 2V max voltage, some output less. Some saturate at 50uW power @ 100kHz and 1064nm. Some saturate at higher power using same swept source

digitizer can have varying gdynamic ranges, some fixed at 400mV, some can adjust between 100mV and 2V

digitizer are usually 12bit, i.e., dynamic range is [0,4095], some read out at this range, but some readout at [0,65535] range, but step size will be 16 instead of 1

digitizer noise is usually small, let's assume the noise (std) is about 0.1 digits in [0,4095] range, i.e., 0.1/4095. 

balanced detector noise is about 10 times higher than digitizer noise. This is what I learnt when analysing a balanced detector and a digitizer in SUSTECH. Some detector can be less or more noisy, 10 times is a rough number

So when we consider the SSOCT system noise, which consists of the detector noise and digitizer noise, usually it should be (digitizer noise in time domain) * (ratio of detector + digitizer noise over digitizer noise) = 0.1/4096 * (10+1) = 0.00027 (what is the unit here? The unit should be ratio of normalized digitizer dynamic range)

For SSOCT we usually care about the frequency domain noise, i.e., in spatial domain. To get that we need to perform FFT on the time domain signal.

FFT result should be (half, because of positive and negative frequency) the amplitude of specific frequency in the original signal. The relationship between frequency domain and time domain is : A/2*exp(-i * k*z ) + A/2*exp(i * k*z ) = Acos(k*z), A is the amplitude of frequency k in SSOCT signal

To do FFT in matlab or python, you usually need to do fs = fft(s)/length(s) to get the correct amplitude. For example, if the amplitude of frequency k0 in the signal is 1, and the number of samples is 1024, you need to do fs = fft(s)/1024 to get value of 1/2 at k0

However, if doing that, the noise before and after FFT is not correctly scaled. To get correctly scaled noise, you need to do fs = fft(s)/sqrt(length(s)), sqrt() means taking the square root. And even if you do that , the noise BEFORE and AFTER FFT will have a ratio of about 2.155, why this number? You need to dig deep into the FFT algorithm

So, if you are doing tranditionally, fs = fft(s)/length(s), the noise BEFORE and AFTER FFT will have an ratio of 2.155 * sqrt(length(s)), the noise BEFORE FFT will be larger.

So get back to noise in SSOCT system, the system noise before FFT was 0.00027, if you are doing 2048 samples, the noise after FFT will be 0.00027/2.155/sqrt(2048) = 2.8e-6

The SSPSOCT system I built at BU has about 4e-5 system noise








Now what about shot noise of ref arm.

shot noise of power P is sqrt(P*t/hv)*hv = sqrt(P*t*hv), unit is J, for 15uW at 1064nm, photon energy is about 2*e-19 J, when sampling at 500MHz, the shot noise is sqrt(15e-6(W) *1/500e6(s) * (2e-19J)) =sqrt(6e-33) = 0.77e-16 J, note that power is P*t = 15e-6/500e6=3e-14, so noise is about 0.25% of power, i.e., 0.0375uW

calculating shot noise at unit of J/sqrt(s), or more frequently used in NEP, W/sqrt(Hz), shot noise = sqrt(P/hv)*hv, for 15uW at 1064uW, the shot noise is sqrt(15e-6*2e-19) = sqrt(3e-24) = 1.7e-12  W/sqrt(Hz), to get the value in unit W, we need to multiply the sqrt root of sampling frequency, 1.7e-12*sqrt(500e6) = 3.8e-8W = 0.038uW , same result  

Thorlabs balanced detector has a noise equivilent power (NEP) at about 15pW/sqrt(Hz), which is almost 10 times higher than the shot noise at 15uW. To get NEP level shot noise, you will need about 100 times higher light power (noise is linear to the sqrt of power), which is 1500uW!!!!!!!!!!!!!!!!!!

However, if you consider a second balanced detector with 2.5pW/Hz^0.5 NEP, you only need 42uW to reach shot noise limited performance

So, SSOCT system using balanced detector and digitizer is not necessarily SHOT NOISE LIMITED, it largely depend on the balanced detector NEP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Literature agreement can be found at https://www.nature.com/articles/s41598-017-01339-6, and cite" For example, standard photodiodes used in the traditional OCT systems at 1300 nm, need a reference power in the order of few miliwatts to approach close to shot-noise-limited sensitivities"


