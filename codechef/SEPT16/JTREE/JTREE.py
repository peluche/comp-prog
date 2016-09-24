def cut_friendless_branch(n, graph, start, friends):
    seen = set((start,))
    stack = [start]
    exit_stack = []
    alives = [False] * (n + 1)
    
    while stack:
        node = stack.pop()
        exit_stack.append(node)
        childs = set()
        for child in graph[node]:
            if child not in seen:
                childs.add(child)
                seen.add(child)
                stack.append(child)
        graph[node] = childs

    while exit_stack:
        node = exit_stack.pop()
        if node in friends: alives[node] = True
        for child in list(graph[node]):
            if alives[child]:
                alives[node] = True
            else:
                graph[node].remove(child)

def build_parents(n, tree):
    parents = [None] * (n + 1)
    for node, childs in enumerate(tree):
        for child in childs:
            parents[child] = node
    return parents

def build_tree(n, xss):
    paths = [set() for _ in range(n + 1)]
    for a, b in xss:
        paths[a].add(b)
        paths[b].add(a)
    return paths

def build_tickets(n, yss):
    tickets = [[] for _ in range(n + 1)]
    for v, k, w in yss:
        tickets[v].append((w, k))
    for ticket in tickets:
        ticket.sort()
    return tickets

def compute_prices(n, nodes, tickets, parents):
    '''
    Everything had to be rewritten in an iterative style otherwise
    it was blowing the stack.
    '''
    prices = [float('inf')] * (n + 1)
    prices[1] = 0
    stack = [1]
    segment_tree = make_segment_tree(0, n + 1)
    path = 0
    while stack:
        node = stack.pop()
        if node == -1:
            update_leaf(segment_tree, path, float('inf'))
            path -= 1
            continue
        stack.append(-1)
        mini = prices[node]

        for w, k in tickets[node]:
            if w >= mini: break
            min_range = read_interval(segment_tree, path - k + 1, path) # XXX
            if min_range + w < mini: mini = min_range + w
        prices[node] = mini
        path += 1
        update_leaf(segment_tree, path, mini)
        for child in nodes[node]:
            stack.append(child)
    return prices

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.val = float('inf')

def update_leaf(node, index, val):
    if node.start == node.end:
        assert node.start == index
        node.val = val
        return
    mid = (node.start + node.end) / 2
    if index <= mid: update_leaf(node.left, index, val)
    else: update_leaf(node.right, index, val)
    node.val = min(node.left.val, node.right.val)
    # if node.start > index or node.end < index: return node.val
    # elif node.start >= start and node.end <= end: return node.val
    # l = read_interval(node.left, start, end)
    # r = read_interval(node.right, start, end)
    # return min(l, r)

def read_interval(node, start, end):
    if node.start > end or node.end < start: return float('inf')
    elif node.start >= start and node.end <= end: return node.val
    l = read_interval(node.left, start, end)
    r = read_interval(node.right, start, end)
    return min(l, r)

def make_segment_tree(start, end):
    node = Node(start, end)
    if start == end: return node
    mid = (start + end) / 2
    node.left = make_segment_tree(start, mid)
    node.right = make_segment_tree(mid + 1, end)
    return node

def solve(n, xss, yss, qs):
    tickets = build_tickets(n, yss)
    tree = build_tree(n, xss)
    cut_friendless_branch(n, tree, 1, set(qs))
    parents = build_parents(n, tree)
    prices = compute_prices(n, tree, tickets, parents)
    return '\n'.join(str(prices[q]) for q in qs)

if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    xss = [map(int, raw_input().split()) for _ in range(n - 1)]
    yss = [map(int, raw_input().split()) for _ in range(m)]
    qs = [int(raw_input()) for _ in range(int(raw_input()))]
    print solve(n, xss, yss, qs)

def test():
    N = 10**5
    M = N
    Q = N
    W = 10**9
    import random
    r = random.randrange
    xss = zip(range(1, N), range(2, N + 1))
    # yss = zip(range(2, M + 1), [M] * M, [r(1, W) for _ in range(M)])
    yss = zip(range(2, M + 1), [r(1, M) for _ in range(M)], [r(1, W) for _ in range(M)])
    qs = range(1, Q + 1)
    # Serialize to Codechef input format
    # ----------------------------------
    print N, M - 1
    print '\n'.join('{} {}'.format(x, y) for x, y in xss)
    print '\n'.join('{} {} {}'.format(x, y, z) for x, y, z in yss)
    print len(qs)
    print '\n'.join(str(x) for x in qs)
    # ----------------------------------
    res = solve(N, xss, yss, qs)
    # print res

# test()
# import cProfile
# cProfile.run('test()')
