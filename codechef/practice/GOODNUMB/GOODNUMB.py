import math

def squares(upper=10**5):
    """ is n square free """
    nums = [True] * (upper + 1)
    nums[0] = False
    for i in range(2, (upper + 3) / 2):
        sq = i * i
        for j in range(sq, upper + 1, sq):
            nums[j] = False
    return nums

def divisors_sum(upper=10**5):
    """ sum of divisors for n """
    nums = [0] * (upper + 1)
    for i in range(1, upper + 1):
        for j in range(i, upper + 1, i):
            nums[j] += i
    return nums

def omega_primes(upper=10**5):
    """ number of prime divisors for n """
    nums = [0] * (upper + 1)
    for i in range(2, upper + 1):
        if nums[i] != 0: continue
        for j in range(i, upper + 1, i):
            nums[j] += 1
    return nums

def sieve(upper=10**5):
    """ number of prime divisors for n """
    nums = [True] * (upper + 1)
    nums[0] = False
    nums[1] = False
    for i in range(2, upper + 1):
        if not nums[i]: continue
        for j in range(i * 2, upper + 1, i):
            nums[j] = False
    return nums

def prefix_sum(upper=10**5):
    ''' A sieve in a sieve in a sieve '''
    sums = divisors_sum(upper)
    square_free = squares(upper)
    omega = omega_primes(max(sums))
    primes = sieve(max(omega))
    nums = [0] * (upper + 1)
    total = 0
    for i, s in enumerate(sums):
        if square_free[i] and primes[omega[s]]:
            total += s
        nums[i] = total
    return nums

if __name__ == '__main__':
    psums = prefix_sum()
    for _ in range(int(raw_input())):
        l, r = map(int, raw_input().split())
        print '{}'.format(psums[r] - psums[l - 1])

