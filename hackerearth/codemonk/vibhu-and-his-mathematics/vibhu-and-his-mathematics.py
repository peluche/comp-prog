MOD = 1000000007

def solve(xs):
    n = max(xs)
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2]) % MOD
    return '\n'.join((str(dp[x]) for x in xs))

if __name__ == '__main__':
    t = int(raw_input())
    print solve([int(raw_input()) for _ in range(t)])
