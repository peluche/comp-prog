import collections
import heapq

def mst(graph, n):
    total = 0
    seen = set([1])
    q = graph[1]
    heapq.heapify(q)
    while q:
        cost, node = heapq.heappop(q)
        if node in seen: continue
        seen.add(node)
        total += cost
        if len(seen) == n: break
        for child in graph[node]:
            heapq.heappush(q, child)
    return total

def solve(n, mss):
    graph = collections.defaultdict(list)
    for a, b, cost in mss:
        graph[a].append((-cost, b))
        graph[b].append((-cost, a))
    mini = mst(graph, n)
    return -mini

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        n, m = map(int, raw_input().split())
        mss = [map(int, raw_input().split()) for _ in range(m)]
        print solve(n, mss)
