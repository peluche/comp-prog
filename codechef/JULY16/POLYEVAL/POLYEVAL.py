MOD = 786433

def omega(n):
    ''' we need to reduce w according to the domain n '''
    # compute the log2(n)
    n /= 3
    log_2_n = -1
    while n > 0:
        log_2_n += 1
        n /= 2
    return pow(10, 2**(18 - log_2_n), MOD)

def fft2(signal):
    n = len(signal)
    if n == 3:
        w1 = pow(10, 2**18, MOD)
        w2 = pow(10, 2 * 2**18, MOD)
        w4 = pow(10, 4 * 2**18, MOD)
        return [
            signal[0] + signal[1] + signal[2],
            signal[0] + signal[1] * w1 + signal[2] * w2,
            signal[0] + signal[1] * w2 + signal[2] * w4
        ]
    else:
        Feven = fft2(signal[0::2])
        Fodd  = fft2(signal[1::2])
        combined = [0] * n
        w = omega(n)
        power = 1
        for m in xrange(n/2):
            tmp = power * Fodd[m]
            power = (power * w) % MOD
            combined[m] = (Feven[m] + tmp) % MOD
            combined[m + n/2] = (Feven[m] - tmp) % MOD

        return combined

def lookup():
    look = {}
    for k in range(MOD - 1):
        val = pow(10, k, MOD)
        if val not in look:
            look[val] = k
    return look

def solve(n, coefs, qs):
    '''
    The solution use the DST step of Number theoretic transform (NTT)
    to generate all values between 1 and MOD
    '''
    ncoefs = coefs + ([0] * (MOD - 1 - len(coefs)))
    ffts = fft2(ncoefs)
    look = lookup()

    # append the value for f(0) as it is not in the range [1, MOD]
    ffts.append(coefs[0])
    look[0] = len(ffts) - 1
    
    res = []
    for q in qs:
        val = ffts[look[q]]
        res.append(val)
    return '\n'.join((str(x) for x in res))
        
if __name__ == '__main__':
    N = int(raw_input())
    coefs = map(int, raw_input().split())
    Q = int(raw_input())
    qs = []
    for _ in range(Q):
        qs.append(int(raw_input()))
    res = solve(N, coefs, qs)
    print '{}'.format(res)

# def horner(coefs, q):
#     ''' Evaluate a polynomial of degre N in O(N) '''
#     val = 0
#     for coef in reversed(coefs):
#         val = (val * q + coef) % MOD
#     return val
    
# see. http://www.apfloat.org/ntt.html
# ---
# p = k * n + 1
# 786433 = 3 * 2**18 + 1
# ---
# w = r ** k (mod p)
# w = 10 ** 3 % 786433

# def transform_radix2(vector):
#     ''' see. https://www.nayuki.io/res/free-small-fft-in-multiple-languages/fft.py '''
#     vector = vector[:]
#     # Returns the integer whose value is the reverse of the lowest 'bits' bits of the integer 'x'.
#     def reverse(x, bits):
#         y = 0
#         for i in range(bits):
#             y = (y << 1) | (x & 1)
#             x >>= 1
#         return y
    
#     # Initialization
#     n = len(vector)
#     levels = 0
#     while True:
#         if 1 << levels == n:
#             break
#         elif 1 << levels > n:
#             raise ValueError("Length is not a power of 2")
#         else:
#             levels += 1
#     # Now, levels = log2(n)
#     exptable = [pow(10**3, i, MOD) for i in range(n // 2)]
#     vector = [vector[reverse(i, levels)] for i in range(n)]  # Copy with bit-reversed permutation
    
#     # Radix-2 decimation-in-time FFT
#     size = 2
#     while size <= n:
#         halfsize = size // 2
#         tablestep = n // size
#         for i in range(0, n, size):
#             k = 0
#             for j in range(i, i + halfsize):
#                 temp = vector[j + halfsize] * exptable[k]
#                 vector[j + halfsize] = (vector[j] - temp) % MOD
#                 vector[j] = (vector[j] + temp) % MOD
#                 k += tablestep
#         size *= 2
#     return vector
