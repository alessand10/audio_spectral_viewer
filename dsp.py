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

def twiddle(N, divisor, exp_mult):
    exp = 2 * math.pi * (divisor/N) * exp_mult
    return math.cos(exp) - 1.0j*math.sin(exp)


def A(m, x):
    N_div_2 = len(x) / 2 - 1
    result = 0 + 0j
    for n in range(0, N_div_2):
        result += x[2*n] * (twiddle(2, len(x)/2, m * n))

    return result

def B(m, x):
    N_div_2 = len(x) / 2 - 1
    result = 0 + 0j
    for n in range(0, N_div_2):
        result += x[2*n + 1] * (2, twiddle(len(x)/2, m * n))

    return result



# Ensure the size of the input is a power of 2
def fft(input):
    output = []
    N = len(input)
    levels = math.log2(input)
