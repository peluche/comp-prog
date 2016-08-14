import collections
import heapq

def mst(graph, n):
    total = 0
    seen_m = set([1])
    seen_f = set([1])
    q = graph[1]
    heapq.heapify(q)
    while q:
        used = False
        kind, node = heapq.heappop(q)
        # if node in seen_m and node in seen_f: continue
        if kind in (-1, -3) and node not in seen_m:
            seen_m.add(node)
            used = True
        if kind in (-2, -3) and node not in seen_f:
            seen_f.add(node)
            used = True
        if not used: continue
        total += 1
        if len(seen_m) == n and len(seen_f) == n: break
        for child in graph[node]:
            heapq.heappush(q, child)
    if len(seen_m) != n or len(seen_f) != n: return -1
    return total

def solve(n, mss):
    graph = collections.defaultdict(list)
    for a, b, kind in mss:
        graph[a].append((-kind, b))
        graph[b].append((-kind, a))
    mini = mst(graph, n)
    if mini == -1: return -1
    return len(mss) - mini

if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    mss = [map(int, raw_input().split()) for _ in range(m)]
    print solve(n, mss)
