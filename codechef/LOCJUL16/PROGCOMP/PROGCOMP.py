import collections

MOD = 1000000007

def facm(n):
    fac = 1
    for i in range(1, n + 1):
        fac = (fac * i) % MOD
    return fac

def solve(xs):
    count = collections.Counter(xs)
    team_permutations = facm(len(count))
    for v in count.values():
        team_permutations = (team_permutations * facm(v)) % MOD
    return team_permutations

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print solve(raw_input())
