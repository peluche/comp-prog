MOD = 1000000007
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)

def running_hash(s, prime):
    ''' Computes the running hash of the string '''
    vals = map(ord, s)
    for i in range(1, len(vals)):
        vals[i] = (vals[i - 1] * prime + vals[i]) % MOD
    return vals

def range_hash(hashs, prime, start, end):
    h = hashs[end]
    if start > 0:
        prefix_hash = (hashs[start - 1] * pow(prime, end - start + 1, MOD)) % MOD
        h = (h - prefix_hash) % MOD
    return h

def solve(s, xss):
    ''' Using several primes as seed for the running hash to reduce collisions '''
    res = []
    hs = [(prime, running_hash(s, prime)) for prime in PRIMES]
    for l1, r1, l2, r2 in xss:
        equals = True
        for prime, hashs in hs:
            h1 = range_hash(hashs, prime, l1 - 1, r1 - 1)
            h2 = range_hash(hashs, prime, l2 - 1, r2 - 1)
            if h1 != h2:
                equals = False
                break
        res.append('Yes' if equals else 'No')
    return '\n'.join(res)

if __name__ == '__main__':
    s = raw_input()
    xss = [map(int, raw_input().split()) for _ in range(int(raw_input()))]
    print solve(s, xss)
