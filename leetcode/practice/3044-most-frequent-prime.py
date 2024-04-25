from collections import Counter

def sieve(maxi):
    nums = list(range(maxi + 1))
    for i in range(2, int(maxi ** 0.5) + 1):
        if not nums[i]: continue
        multiple = i * 2
        while multiple <= maxi:
            nums[multiple] = 0
            multiple += i
    return {num for num in nums if num > 10}

PRIMES = sieve(999999)
DIRS = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

def walk(mat, i, j, dir, counter):
    di, dj = dir
    last = 0
    while -1 < i < len(mat) and -1 < j < len(mat[0]):
        last = last * 10 + mat[i][j]
        if last in PRIMES:
            counter[last] += 1
        i += di
        j += dj

def walk_all_dirs(mat, i, j, counter):
    for dir in DIRS:
        walk(mat, i, j, dir, counter)

def walk_all(mat, counter):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            walk_all_dirs(mat, i, j, counter)

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        counter = Counter()
        walk_all(mat, counter)
        vals = [(cnt, prime) for prime, cnt in counter.items()]
        if not vals: return -1
        return max(vals)[1]
