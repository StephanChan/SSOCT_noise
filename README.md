# SSOCT_noise
noise and SNR analysis of swept source OCT that use a balanced detector and digitizer for readout

Different balanced detector can have different gains, some output 2V max voltage, some output less. Some saturate at 50uW power @ 100kHz and 1064nm. Some saturate at higher power using same swept source

digitizer can have varying gains, some fixed at 400mV, some can adjust between 100mV and 2V

digitizer are usually 12bit, i.e., dynamic range is [0,4095], but they readout at 16bit, so the displayed dynamic range is [0,65535], but step size will be 16 instead of 1

digitizer noise is usually small, let's assume the noise (std) is about 2 digits in [0,4095] range, i.e., 2/4095. In reality it could be slightly smaller than that, at least for the Alazar and ALT digitizers I used

balanced detector noise is about 10 times higher than digitizer noise

So when we consider the SSOCT system noise, which consists of the detector noise and digitizer noise, usually it should be (digitizer noise in time domain) * (ratio of detector + digitizer noise over digitizer noise) = 2/4096 * (10+1) = 0.0054 (what is the unit here? The unit should be ratio of normalized digitizer dynamic range)

For SSOCT we usually care about the frequency domain noise, i.e., in spatial domain. 

FT is an interesting process, the FT result is (half, because of positive and negative frequency) the amplitude of specific frequency in the original signal. The relationship between frequency domain and time domain is : A/2*exp(-i * k*z ) + A/2*exp(i * k*z ) = A, A is the amplitude of frequency k in SSOCT signal

To do FFT in matlab or python, you usually need to do fs = fft(s)/length(s) to get the correct amplitude. For example, if the amplitude of frequency k0 in the signal is 1, and the number of samples is 1024, you need to do fs = fft(s)/1024 to get value of 1/2 at k0

However, if doing that, the noise before and after FFT is not correctly scaled. To get correctly scaled noise, you need to do fs = fft(s)/sqrt(length(s)), sqrt() means taking the square root. And even if you do that , the noise BEFORE and AFTER FFT will have a ratio of about 2.155, why this number? You need to dig deep into the FFT algorithm

So, if you are doing tranditionally, fs = fft(s)/length(s), the noise BEFORE and AFTER FFT will have an ratio of 2.155 * sqrt(length(s)), the noise BEFORE FFT will be larger.

So get back to noise in SSOCT system, the system noise before FFT was 0.0054, if you are doing 2048 samples, the noise after FFT will be 0.0054/2.155/sqrt(2048) = 5.5e-5
