def solve(xss):
    dp = [[0] * len(xss) for i in range(3)]
    dp[0][0] = xss[0][0]
    dp[1][0] = xss[0][1]
    dp[2][0] = xss[0][2]
    for i, xs in enumerate(xss[1:], 1):
        dp[0][i] = xs[0] + min(dp[1][i - 1], dp[2][i - 1])
        dp[1][i] = xs[1] + min(dp[0][i - 1], dp[2][i - 1])
        dp[2][i] = xs[2] + min(dp[0][i - 1], dp[1][i - 1])
    return min(dp[0][-1], dp[1][-1], dp[2][-1])

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        n = int(raw_input())
        xss = [map(int, raw_input().split()) for _ in range(n)]
        print solve(xss)
