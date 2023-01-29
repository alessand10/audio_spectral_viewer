from playsound import playsound
from scipy.io import wavfile
import matplotlib as mpl
import matplotlib.pyplot as plt
import dsp
import time


fs, data = wavfile.read('C:/Users/Alessandro Genovese/Downloads/The Killers - Mr. Brightside (Two Friends Remix).wav')
N = 735
frame = 105

data_L = [x[0] for x in data[frame * N:(frame+1) * N]]
data_R = [x[1] for x in data[frame * N:(frame+1) * N]]

current_time = time.time()
magnitudes = dsp.dft(data_L)
frequencies = []
amplitudes = []
f_nyquist = fs / 2

for index in range(1, int(N)):
    freq = fs/N * index
    if freq >= 6000:
        break
    frequencies.append(freq)
    amplitudes.append(round(abs(magnitudes[index] / N * 2), 2))



print(time.time() - current_time)

p = plt.plot(frequencies, amplitudes)
plt.xlabel("Frequency(Hz)")
plt.ylabel("Amplitude")
plt.show()
