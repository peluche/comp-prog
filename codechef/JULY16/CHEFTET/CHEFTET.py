def greedy(xs, bs, goal):
    used = [False] * len(bs)
    for i, val in enumerate(xs):
        if i > 0 and not used[i - 1]:
            val += bs[i - 1]
        if val == goal: continue
        elif not used[i] and val + bs[i] == goal:
            used[i] = True
        elif not used[i + 1] and val + bs[i + 1] == goal:
            used[i + 1] = True
        elif not used[i] and not used[i + 1] and val + bs[i] + bs[i + 1] == goal:
            used[i] = True
            used[i + 1] = True
        else: return -1
    if used[len(xs) - 1] != True: return -1
    return goal
        
def solve(xs, bs):
    bs.append(0)
    return max(
        greedy(xs, bs, xs[0]),
        greedy(xs, bs, xs[0] + bs[0]),
        greedy(xs, bs, xs[0] + bs[1]),
        greedy(xs, bs, xs[0] + bs[0] + bs[1]))
    
if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _ = int(raw_input())
        BS = map(int, raw_input().split())
        AS = map(int, raw_input().split())
        res = solve(AS, BS)
        print '{}'.format(res)
