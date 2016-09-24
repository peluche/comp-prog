import random
import time
 
def make_query(dp):
    def ret(ax, ay, bx, by):
        ax, ay, bx, by = ax + 1, ay + 1, bx + 1, by + 1
        return dp[by][bx] - dp[ay - 1][bx] - dp[by][ax - 1] + dp[ay - 1][ax - 1]
 
    return ret
 
def make_rect_query(xss):
    dp = [[0] * (len(xss) + 1)]
    for xs in xss:
        dp.append([0] + xs)
    for i in range(1, len(dp)):
        for j in range(1, len(dp)):
            dp[i][j] += dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
    return dp
 
def randn(n, p):
    return random.sample(xrange(1, n), p)
 
def brute_score(query, sorted_hz, sorted_vt):
    maxi = 0
    for ax, bx in zip(sorted_vt, sorted_vt[1:]):
        for ay, by in zip(sorted_hz, sorted_hz[1:]):
            cost = query(ax, ay, bx - 1, by - 1)
            if cost > maxi: maxi = cost
    return maxi
 
def score_all(query, sorted_hz, sorted_vt):
    scores = []
    ys = list(zip(sorted_hz, sorted_hz[1:]))
    xs = list(zip(sorted_vt, sorted_vt[1:]))
    for ay, by in ys:
        for ax, bx in xs:
            scores.append(query(ax, ay, bx - 1, by - 1))
    return scores
 
 
def brute_hillclimbing(query, hz, vt, start_time):
    separators = (hz, vt)
    score = brute_score(query, hz, vt)
    # it = 0 # XXX
    while time.time() - start_time < 1.8:
        # it += 1 # XXX
        separator = random.choice(separators)
        idx = random.randrange(1, len(separator) - 1)
        old_val = separator[idx]
        new_val = random.randrange(separator[idx - 1] + 1, separator[idx + 1])
        if old_val == new_val: continue
        separator[idx] = new_val
        new_score = brute_score(query, hz, vt)
        if new_score <= score:
            score = new_score
        else:
            separator[idx] = old_val
    # print 'iterations: ', it # XXX
 
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.val = None
 
def make_segment_tree(xs, start, end):
    node = Node(start, end)
    if start == end:
        node.val = xs[start]
        return node
    mid = (start + end) / 2
    node.left = make_segment_tree(xs, start, mid)
    node.right = make_segment_tree(xs, mid + 1, end)
    node.val = max(node.left.val, node.right.val)
    return node
 
def update_leaf(node, index, val):
    if node.start == node.end:
        node.val = val
        return
    mid = (node.start + node.end) / 2
    if index <= mid: update_leaf(node.left, index, val)
    else: update_leaf(node.right, index, val)
    l = node.left.val
    r = node.right.val
    node.val = l if l >= r else r
 
def update_leaf_it(node, index, val):
    stack = []
    while node.start != node.end:
        stack.append(node)
        mid = (node.start + node.end) / 2
        node = node.left if index <= mid else node.right
    node.val = val
    while stack:
        node = stack.pop()
        node.val = max(node.left.val, node.right.val)
    
def update_st(query, st, separators, direction, idx):
    hz, vt = separators
    l = len(hz) - 1
    xs = list(zip(range(l), vt, vt[1:]))
    ys = list(zip(range(l), hz, hz[1:]))
 
    if direction == 0: # changed horizontal
        ys = ys[idx - 1:idx + 1]
    else: # changed vertical
        xs = xs[idx - 1:idx + 1]
    
    for x, ax, bx in xs:
        for y, ay, by in ys:
            cost = query(ax, ay, bx - 1, by - 1)
            idx = x + y * l
            update_leaf_it(st, idx, cost)
 
def make_fake_st(scores):
    n = len(scores)
    st = ([0] * n) + scores
    for i in range(n - 1, 0, -1):
        st[i] = max(st[i<<1], st[i<<1|1])
    return st
 
def update_fake_leaf(st, idx, cost):
    i = idx + len(st) / 2
    st[i] = cost
    while i > 1:
        st[i>>1] = max(st[i], st[i^1])
        i >>= 1
 
def update_fake_st(query, st, separators, direction, idx):
    hz, vt = separators
    l = len(hz) - 1
    xs = list(zip(range(l), vt, vt[1:]))
    ys = list(zip(range(l), hz, hz[1:]))
 
    if direction == 0: # changed horizontal
        ys = ys[idx - 1:idx + 1]
    else: # changed vertical
        xs = xs[idx - 1:idx + 1]
 
    ops = []
    maxi = st[1]
    for x, ax, bx in xs:
        for y, ay, by in ys:
            cost = query(ax, ay, bx - 1, by - 1)
            if cost > maxi: return False
            idx = x + y * l
            ops.append((idx, cost))
    for idx, cost in ops:
        update_fake_leaf(st, idx, cost)
    return True
 
    # for x, ax, bx in xs:
    #     for y, ay, by in ys:
    #         cost = query(ax, ay, bx - 1, by - 1)
    #         idx = x + y * l
    #         update_fake_leaf(st, idx, cost)
 
 
 
def hillclimbing(query, hz, vt, start_time):
    separators = (hz, vt)
    scores = score_all(query, hz, vt)
    # st = make_segment_tree(scores, 0, len(scores) - 1)
    # score = st.val
    st = make_fake_st(scores)
    score = st[1]
    # score = brute_score(query, hz, vt) # XXX
    # score2 = brute_score(query, hz, vt) # XXX
    # assert score == score2, '{} {}'.format(score, score2) # XXX
    # it = 0 # XXX
    # op = 0 # XXX
    # nop = 0 # XXX
    while time.time() - start_time < 4.8:
        # it += 1 # XXX
        direction = random.randrange(0, 2)
        separator = separators[direction]
        idx = random.randrange(1, len(separator) - 1)
        old_val = separator[idx]
        new_val = random.randrange(separator[idx - 1] + 1, separator[idx + 1])
        if old_val == new_val: continue
        separator[idx] = new_val
        # update_st(query, st, separators, direction, idx)
        # new_score = st.val
        ret = update_fake_st(query, st, separators, direction, idx)
        # new_score = st[1]
        # new_score = brute_score(query, hz, vt) # XXX
        # new_score2 = brute_score(query, hz, vt) # XXX
        # assert new_score == new_score2 # XXX
 
        if ret:
            score = st[1]
            # op += 1
        else:
            separator[idx] = old_val
            # nop += 1
 
        # if new_score <= score:
        #     score = new_score
        #     op += 1 # XXX
        # else:
        #     separator[idx] = old_val
        #     # update_st(query, st, separators, direction, idx)
        #     # new_score = st.val
        #     update_fake_st(query, st, separators, direction, idx)
        #     new_score = st[1]
        #     # new_score = brute_score(query, hz, vt) # XXX
        #     # new_score2 = brute_score(query, hz, vt) # XXX
        #     # assert new_score == new_score2 # XXX
        #     nop += 1 # XXX
    # print 'iterations {} op {} nop {} '.format(it, op, nop) # XXX
 
def hillclimbing2(query, hz, vt, start_time):
    separators = (hz, vt)
    # scores = score_all(query, hz, vt)
    # st = make_segment_tree(scores, 0, len(scores) - 1)
    # score = st.val
    score = brute_score(query, hz, vt) # XXX
    # score2 = brute_score(query, hz, vt) # XXX
    # assert score == score2 # XXX
    it = 0 # XXX
    op = 0 # XXX
    nop = 0 # XXX
    # while time.time() - start_time < 1.8:
    while time.time() - start_time < 5:
        it += 1 # XXX
        direction = random.randrange(0, 2)
        separator = separators[direction]
        idx = random.randrange(1, len(separator) - 1)
        old_val = separator[idx]
        new_val = random.randrange(separator[idx - 1] + 1, separator[idx + 1])
        if old_val == new_val: continue
        separator[idx] = new_val
        # update_st(query, st, separators, direction, idx)
        # new_score = st.val
        new_score = brute_score(query, hz, vt) # XXX
        # new_score2 = brute_score(query, hz, vt) # XXX
        # assert new_score == new_score2 # XXX
        if new_score <= score:
            score = new_score
            op += 1 # XXX
        else:
            separator[idx] = old_val
            # update_st(query, st, separators, direction, idx)
            # new_score = st.val
            new_score = brute_score(query, hz, vt) # XXX
            # new_score2 = brute_score(query, hz, vt) # XXX
            # assert new_score == new_score2 # XXX
            nop += 1 # XXX
    print 'iterations {} op {} nop {} '.format(it, op, nop) # XXX
    
def solve(n, p, xss):
    p -= 1
    start_time = time.time()
    query = make_query(make_rect_query(xss))
    hz = sorted([0] + randn(n, p) + [n])
    vt = sorted([0] + randn(n, p) + [n])
    # print hz, vt
    # print 'before:', brute_score(query, hz, vt)
    # brute_hillclimbing(query, hz, vt, start_time)
    # hillclimbing2(query, hz, vt, start_time)
    hillclimbing(query, hz, vt, start_time)
    # print 'after: ', brute_score(query, hz, vt)
    return '\n'.join((' '.join(str(h) for h in hz[1:-1]),
                     ' '.join(str(v) for v in vt[1:-1])))
 
if __name__ == '__main__':
    n, p = map(int, raw_input().split())
    xss = [map(int, raw_input().split()) for _ in range(n)]
    print solve(n, p, xss)
 
def test():
    N = 500
    P = 400
    xss = [[random.randrange(1, 10**9) for _ in range(N)] for _ in range(N)]
    res = solve(N, P, xss)
    # print res
 
# import cProfile
# cProfile.run('test()')
# test()
