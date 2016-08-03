def dfs(graph, root):
    seen = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if node in seen: continue
        seen.add(node)
        for friend in graph[node]:
            stack.append(friend)
    return len(seen)

def solve(friend_count, xss):
    graph = {i: [] for i in range(1, friend_count + 1)}
    for x, y in xss:
        graph[x].append(y)
    mini = float("inf")
    for friend in graph.keys():
        mini = min(mini, dfs(graph, friend))
    return mini

if __name__ == '__main__':
    n, d = map(int, raw_input().split())
    print solve(n, [map(int, raw_input().split()) for _ in range(d)])
