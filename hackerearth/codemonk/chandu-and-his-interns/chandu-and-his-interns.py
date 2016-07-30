def sieve_ish(n):
    ''' too slow with CPython make PYPY available! >:( '''
    divisors = [1] * (n + 2)
    for i in range(2, n + 2):
        if divisors[i] < 4:
            for j in range(i, n + 2, i):
                divisors[j] += 1
    return divisors

def solve(xs):
    divisors = sieve_ish(max(xs))
    return '\n'.join('NO' if divisors[x] < 4 else 'YES' for x in xs)

if __name__ == '__main__':
    print solve([int(raw_input()) for _ in range(int(raw_input()))])
