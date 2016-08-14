import collections
import heapq

def solve(xss):
    res = []
    counts = collections.defaultdict(lambda: 0)
    min_q = []
    max_q = []
    for xs in xss:
        if xs[0] == 1:
            counts[xs[1]] += 1
            heapq.heappush(min_q, xs[1])
            heapq.heappush(max_q, -xs[1])
        elif xs[0] == 2:
            if not counts[xs[1]]: res.append(-1)
            else: counts[xs[1]] -= 1
        elif xs[0] == 3:
            while len(max_q) and not counts[-max_q[0]]: heapq.heappop(max_q)
            x = -1
            if len(max_q): x = -max_q[0]
            res.append(x)
        elif xs[0] == 4:
            while len(min_q) and not counts[min_q[0]]: heapq.heappop(min_q)
            x = -1
            if len(min_q): x = min_q[0]
            res.append(x)
    return '\n'.join(str(r) for r in res)

if __name__ == '__main__':
    xss = [map(int, raw_input().split()) for _ in range(int(raw_input()))]
    print solve(xss)
