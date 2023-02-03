from playsound import playsound
from scipy.io import wavfile
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import dsp
from PIL import Image
import time
import os


fs, data = wavfile.read('Coldplay X BTS - My Universe (Official Lyric Video).wav')

framerate = 60
width = 750
height = 500
max_f = 8000

# Sample size
N = int(fs*2/framerate)
frame_num = 30

def compute_fourier_transform(frame):
    data_L = [x[0] for x in data[frame * N:(frame+1) * N]]
    data_R = [x[1] for x in data[frame * N:(frame+1) * N]]

    # Pad the values to bring the sample size to 1024 for the FFT
    padding_amount = 1024 - N
    data_L.extend([0]*(padding_amount))

    magnitudes = np.fft.fft(data_L)
    frequencies = []
    amplitudes = []
    f_nyquist = fs / 2

    for index in range(1, int(N)):
        freq = fs/N * index
        if freq >= max_f:
            break
        amplitudes.append(round(abs(magnitudes[index] / N * 2), 2))
    
    return amplitudes


current_time = time.time()
print(time.time() - current_time)

def clamp(x, min, max):
    if x < min:
        return min
    elif x > max:
        return max
    else:
        return x

def basic_colour_profile(norm):
    r = 255 * norm
    b = 255 * (1 - norm)
    return [r, 0, b]
 
def render_frame(amplitudes):
    height_div_2 = height/2
    a = np.zeros([height, width, 3], dtype=np.uint8)
    for col in range(0, width):
        amp_index = int(col * ((len(amplitudes) - 1) / width))
        lit_rows = clamp(int(amplitudes[amp_index]/16384 * height_div_2), 0, height_div_2 - 1)
        for row in range(int(height_div_2 - lit_rows), int(height_div_2 + lit_rows)):
            a[(height - 1) - row, col] = basic_colour_profile(col/width)
            
    return Image.fromarray(a, mode="RGB")

frame_count = int(len(data)/N)
for frame_num in range(0, frame_count):
    render_frame(compute_fourier_transform(frame_num)).save("C:/CodeProjects/audio_spectral_viewer/generated_images/frame{}.png".format(frame_num))

os.system('ffmpeg -itsoffset 0.25 -i "Coldplay X BTS - My Universe (Official Lyric Video).wav" -i generated_images/frame%01d.png -vcodec mpeg4 -y -r 60 -vb 40M movie.mp4')


