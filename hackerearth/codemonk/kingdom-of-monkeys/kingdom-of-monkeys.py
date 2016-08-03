import collections

def dfs(graph, seen, scores, node):
    ''' I got replaced because I broke the recursion limit :'( '''
    if node in seen: return 0
    seen.add(node)
    score = scores[node - 1]
    for child in graph[node]:
        score += dfs(graph, seen, scores, child)
    return score

def dfs_iter(graph, seen, scores, root):
    score = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node in seen: continue
        seen.add(node)
        score += scores[node - 1]
        for child in graph[node]:
            stack.append(child)
    return score

def solve(xss, ys):
    graph = collections.defaultdict(list)
    for x, y in xss:
        graph[x].append(y)
        graph[y].append(x)
    seen = set()
    count = max(ys)
    for x in graph.keys():
        count = max(count, dfs_iter(graph, seen, ys, x))
    return count

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _, m = map(int, raw_input().split())
        xss = [map(int, raw_input().split()) for _ in range(m)]
        ys = map(int, raw_input().split())
        print solve(xss, ys)
