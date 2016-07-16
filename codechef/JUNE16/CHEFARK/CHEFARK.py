MOD = 1000000007

def all_n_choose_k(n, k, zeros):
    do_all = zeros > 0
    total = 0
    incremental_fac_numerator = n
    incremental_fac_denominator = 1
    parity = k % 2
    if do_all or parity == 0:
        total += 1
    if do_all or parity == 1:
        total += incremental_fac_numerator
    for i in range(2, k + 1):
        if i > n: break
        incremental_fac_numerator = (incremental_fac_numerator * (n - i + 1)) % MOD
        incremental_fac_denominator = (incremental_fac_denominator * i) % MOD
        if do_all or i % 2 == parity:
            fac = (incremental_fac_numerator * pow(incremental_fac_denominator, MOD - 2, MOD)) % MOD
            total += fac
    return total % MOD

def solve(n, k, xs):
    zeros = xs.count(0)
    xs_len = len(xs) - zeros
    return all_n_choose_k(xs_len, k, zeros)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        N, K = map(int, raw_input().split())
        XS = map(int, raw_input().split())
        res = solve(N, K, XS)
        print '{}'.format(res)
