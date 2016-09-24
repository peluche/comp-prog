import collections
import copy
import heapq
 
def get_path(parents, t):
    path = []
    node = t
    while node != -1:
        path.append(node)
        node = parents[node]
    return path[::-1]
 
def path_slack(g, path):
    if len(path) < 2: return 0
    slack = float('inf')
    for u, v in zip(path, path[1:]):
        available = g[u][v]
        if available < slack: slack = available
    return slack
 
def add_slack(g, path, slack):
    # assert slack > 0 # XXX
    for u, v in zip(path, path[1:]):
        g[u][v] -= slack
        if g[u][v] != g[u][v]: g[u][v] = 0 # NaN
        g[v][u] += slack
    
def find_path(g, n, s, t):
    parents = [-1] * (n + 1)
    q = collections.deque([s])
    while q:
        node = q.popleft()
        if node == t: break
        for child, available in g[node].items():
            if child == s or parents[child] != -1 or available <= 0: continue
            parents[child] = node
            q.append(child)
    path = get_path(parents, t)
    return path
 
def min_cut(g, n, s, t):
    while True:
        path = find_path(g, n, s, t)
        slack = path_slack(g, path)
        if slack == 0: break
        add_slack(g, path, slack)
 
    cut = []
    seen = set([s])
    q = collections.deque([s])
    while q:
        node = q.popleft()
        for child, available in g[node].items():
            if child in seen: continue
            if available == 0: cut.append((node, child))
            else:
                seen.add(child)
                q.append(child)
    return [(u, v) for u, v in cut if u in seen and v not in seen]
 
def score_cut(g, cut):
    return sum(g[u][v] for u, v in cut)
 
def make_mask_to_graph(s, t, simple_g, lookup):
    def ret(depth, mask):
        g = copy.deepcopy(simple_g)
        for i in range(depth + 1):
            node = lookup[i]
            if mask & (1 << i): # `i` in sink
                g[node][t] = float('inf')
            else: # `i` in source
                g[s][node] = float('inf')
        return g
    return ret
 
def make_residual_to_mask(s, t, lookup):
    def ret(g):
        seen = set([s])
        stack = [s]
        while stack:
            node = stack.pop()
            for child, capacity in g[node].items():
                if capacity > 0 and child not in seen:
                    stack.append(child)
                    seen.add(child)
        mask = 0
        for i, node in enumerate(lookup):
            if node not in seen and node != t:
                mask |= 1 << i
        return mask
    return ret
 
def make_initial_candidates(mask_to_graph, residual_to_mask, n, s, t, simple_g):
    flow, depth, mask = 0, 0, 0
    candidates = [] # (flow, depth, cut_mask)
    for _ in range(2):
        g = mask_to_graph(depth, mask)
        cut = min_cut(g, n, s, t) # TODO: kill infinite flow here
        flow = score_cut(simple_g, cut)
        cut_mask = residual_to_mask(g)
        # print 'mask is {:010b} cut_mask is {:010b} for depth {}'.format(mask, cut_mask, depth)
        heapq.heappush(candidates, (flow, depth + 1, cut_mask))
        mask ^= 1 << depth
    return candidates
 
def simple_kth_max_flow(xss, simple_g, reverse_g, n, k, s, t):
    lookup = range(1, n + 1)
    lookup.remove(s)
    lookup.remove(t)
    mask_to_graph = make_mask_to_graph(s, t, simple_g, lookup)
    residual_to_mask = make_residual_to_mask(s, t, lookup)
    seen = {} # mask: flow
    candidates = make_initial_candidates(mask_to_graph, residual_to_mask, n, s, t, simple_g)
    # candidates = [(0, 0, 0)] # (flow, depth, cut_mask)
    # print 'lookup: {}'.format(lookup)
    while k > 0:
    # while candidates: # DEBUG
        flow, depth, mask = heapq.heappop(candidates)
        # print 'flow {} depth {} mask {:010b}'.format(flow, depth, mask)
        if mask not in seen:
            k -= 1
            last_flow = flow
            seen[mask] = flow
            # print flow, mask # XXX
        if depth == len(lookup): continue
 
        heapq.heappush(candidates, (flow, depth + 1, mask))
        mask ^= 1 << depth
        if mask in seen:
            heapq.heappush(candidates, (seen[mask], depth + 1, mask))
            continue
        g = mask_to_graph(depth, mask)
        cut = min_cut(g, n, s, t) # TODO: kill infinite flow here
        flow = score_cut(simple_g, cut)
        cut_mask = residual_to_mask(g)
        # print 'mask is {:010b} cut_mask is {:010b} for depth {}'.format(mask, cut_mask, depth)
        heapq.heappush(candidates, (flow, depth + 1, cut_mask))
 
    return last_flow
 
def solve(n, m, k, s, t, xss):
    simple_g = [collections.defaultdict(lambda: 0) for _ in range(n + 1)]
    reverse_g = [collections.defaultdict(lambda: 0) for _ in range(n + 1)]
    for u, v, weight in xss:
        simple_g[u][v] += weight
        reverse_g[v][u] += weight
    return simple_kth_max_flow(xss, copy.deepcopy(simple_g), reverse_g, n, k, s, t)
 
if __name__ == '__main__':
    n, m, k = map(int, raw_input().split())
    s, t = map(int, raw_input().split())
    xss = [map(int, raw_input().split()) for _ in range(m)]
 
    print solve(n, m, k, s, t, xss)
