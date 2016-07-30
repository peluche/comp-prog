MOD = 1000000007

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def solve(xs):
    f = 1
    g = xs[0]
    for x in xs:
        f = (f * x) % MOD
        g = gcd(x, g)
    return pow(f, g, MOD)

if __name__ == '__main__':
    raw_input()
    print solve(map(int, raw_input().split()))
