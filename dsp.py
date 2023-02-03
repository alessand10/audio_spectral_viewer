import math
import numpy as np


'''
    Returns the Fourier transform of a discrete sequence, follows the mathematical definition
    of the Discrete Fourier Transform.
'''
def dft(input):
    output = []
    for m in range(0, len(input)):
        N = len(input)
        sum = 0.0 + 0.0j
        for n in range(0, N):
            xn = input[n]
            exp = 2 * math.pi * m * (n/N)
            comp_sinusoid = math.cos(exp) - 1.0j*math.sin(exp)
            sum += comp_sinusoid * xn
        output.append(sum)
    return output 


'''
    Returns the Fourier transform of a discrete sequence using the radix-2 Fast Fourier Transform.
    Requires an input size that is a power of 2.
'''
def fft(input):
    if len(input) == 1:
    # if the input size is 2, we return the trivial 2pt DFT
        return input
    
    # otherwise, further divide the DFT using recursive calls
    else:
        N = len(input)

        # Only solve for the first half of the input, the second half can he obtained from the first
        m = np.arange(0, N//2)

        # compute the twiddle factors for m = [0,..,N//2]
        twiddle_factors = np.exp(-1j * 2 * np.pi * m * 1/N)

        # Obtain the set of even and odd samples 
        even = fft(input[0::2])
        odd = fft(input[1::2])

        return np.concatenate([even + (twiddle_factors * odd), even - (twiddle_factors * odd)])