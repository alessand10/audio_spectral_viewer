import math

'''
    Follows the mathematical definition of the discrete Fourier transform.
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


def fft(input):
    