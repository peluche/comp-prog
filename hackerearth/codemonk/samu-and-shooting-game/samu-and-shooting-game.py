# def score_enough(x, y, n, w, p1, p2):
#     if not p1 and not p2: return
#     if not p1:
#         val = w / y + (1 if w % y else 0)
#         if val <= n: yield (0, val)
#         return
#     if not p2:
#         val = w / x + (1 if w % x else 0)
#         if val <= n: yield (val, 0)
#         return
#     for i in range(n + 1):
#         rest = w - i * x
#         j = rest / y + (1 if rest % y else 0)
#         if j >= 0 and i + j <= n:
#             yield (i, j)
#         if i * x >= w: break

# def pows(n, p):
#     ps = [1] * (n + 1)
#     for i in range(1, n + 1):
#         ps[i] = ps[i - 1] * p
#     return ps

# def exactly_k(n, p):
#     dp = [[1] * (i + 1) for i in range(n + 1)]
#     ps = pows(n, p)
#     mps = pows(n, 1 - p)
#     for among in range(1, n + 1):
#         dp[among][among] = p ** among
#         nCk = 1
#         for k in range(among - 1, 0, -1):
#             nCk = nCk * (k + 1) / (among - k)
#             dp[among][k] = nCk * ps[k] * mps[among - k]
#     return dp

# def atleast_k(n, p):
#     dp = exactly_k(n, p)
#     for among in range(1, n + 1):
#         for k in range(among - 1, 0, -1):
#             dp[among][k] += dp[among][k + 1]
#     return dp            

# def solve2(x, y, n, w, p1, p2):
#     p1 /= 100.0
#     p2 /= 100.0
#     dpx = atleast_k(n, p1) if p1 else [[1] for _ in range(n + 1)]
#     dpy = atleast_k(n, p2) if p2 else [[1] for _ in range(n + 1)]
#     best = 0
#     for i, j in score_enough(x, y, n, w, p1, p2):
#         can_miss = n - i - j
#         for miss in range(can_miss + 1):
#             success_rate = dpx[i + miss][i] * dpy[j + can_miss - miss][j]
#             best = max(best, success_rate)
#     return '{:.6f}'.format(best * 100)

def rec(x, y, n, w, p1, p2, memo):
    if w <= 0: return 1
    if n == 0: return 0
    if memo[n][w] == None:
        memo[n][w] = max(
            p1 * rec(x, y, n - 1, w - x, p1, p2, memo) + (1 - p1) * rec(x, y, n - 1, w, p1, p2, memo),
            p2 * rec(x, y, n - 1, w - y, p1, p2, memo) + (1 - p2) * rec(x, y, n - 1, w, p1, p2, memo))
    return memo[n][w]

def solve(x, y, n, w, p1, p2):
    p1 /= 100.0
    p2 /= 100.0
    memo = [[None] * (w + 1) for _ in range(n + 1)]
    return '{:.6f}'.format(rec(x, y, n, w, p1, p2, memo) * 100)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print solve(*map(int, raw_input().split()))
