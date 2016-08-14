import collections

def bfs(graph):
    seen = set()
    nexts = collections.deque([1])
    while nexts:
        node = nexts.popleft()
        if node in seen: continue
        seen.add(node)
        nexts.extend(graph[node])
    return seen

def solve(n, mss, ns):
    graph = collections.defaultdict(list)
    for i in ns:
        a, b = mss[i - 1]
        graph[a].append(b)
        graph[b].append(a)
    seen = bfs(graph)
    return 'YES' if len(seen) == n else 'NO'

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        n, m = map(int, raw_input().split())
        mss = [map(int, raw_input().split()) for _ in range(m)]
        ns = map(int, raw_input().split())
        print solve(n, mss, ns)
