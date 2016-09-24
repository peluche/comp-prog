def sieve(n):
    primes = []
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i + i, n + 1, i): is_prime[j] = False
    return primes

PRIMES = sieve(10**6)

def least_prime(n, mem={}):
    if n == 1: return 1
    if n in mem: return mem[n]
    for prime in PRIMES:
        if n % prime == 0:
            mem[n] = prime
            return prime
    raise("ups")

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.val = None
        self.least_div = None

def update_segment_tree(node, start, end):
    if node.start > end or node.end < start or node.least_div == 1: return
    if node.start == node.end:
        node.least_div = least_prime(node.val)
        node.val /= node.least_div
        return 
    update_segment_tree(node.left, start, end)
    update_segment_tree(node.right, start, end)
    node.least_div = max(node.left.least_div, node.right.least_div)

def read_interval(node, start, end):
    if node.start > end or node.end < start or node.least_div == 1: return 1
    elif node.start >= start and node.end <= end: return node.least_div
    l = read_interval(node.left, start, end)
    r = read_interval(node.right, start, end)
    return max(l, r)
        
def make_segment_tree(xs, start, end):
    node = Node(start, end)
    if start == end:
        node.val = xs[start - 1]
        node.least_div = least_prime(node.val)
        node.val /= node.least_div
        return node
    mid = (start + end) / 2
    node.left = make_segment_tree(xs, start, mid)
    node.right = make_segment_tree(xs, mid + 1, end)
    node.least_div = max(node.left.least_div, node.right.least_div)
    return node

def solve(xs, xss):
    res = []
    st = make_segment_tree(xs, 1, len(xs))
    for cmd, l, r in xss:
        if cmd == 0: update_segment_tree(st, l, r)
        elif cmd == 1: res.append(read_interval(st, l, r))
    return ' '.join(str(x) for x in res)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _, m = map(int, raw_input().split())
        xs = map(int, raw_input().split())
        xss = [map(int, raw_input().split()) for _ in range(m)]
        print solve(xs, xss)

# def to_dict(node):
#     ''' debug helper: make the segment tree easy to print '''
#     if node == None: return None
#     d = {
#         '_': '[{} - {}]'.format(node.start, node.end),
#         '_maxi': node.maxi,
#         '_lazy_div': node.lazy_div,
#     }
#     if node.left: d['left'] = to_dict(node.left)
#     if node.right: d['right'] = to_dict(node.right)
#     if node.val != None: d['_val'] = node.val
#     return d

# def brute_div(n):
#     for p in PRIMES:
#         if n % p == 0: return p
#     return 1

# def brute_read(xs, l, r):
#     return brute_div(max(xs[l:r+1], key=brute_div))

# def brute_update(xs, l, r):
#     for i in range(l, r + 1):
#         xs[i] /= brute_div(xs[i])

# def brute_solve(xs, xss):
#     xs = [0] + xs
#     res = []
#     for cmd, l, r in xss:
#         if cmd == 0: brute_update(xs, l, r)
#         elif cmd == 1: res.append(brute_read(xs, l, r))
#     return ' '.join(str(x) for x in res)
        
# import random
# r = random.randrange
# A = 10**6
# N = 10**5
# # N = 50
# for _ in range(100):
#     xs = [r(1, A) for _ in range(N)]
#     xss = [(r(2), r(1, N/2), r(N/2, N)) for _ in range(N)]
#     lazy = solve(xs, xss)
#     brute = brute_solve(xs, xss)
#     # brute = lazy
#     try:
#         assert lazy == brute
#     except:
#         print 'xs:', xs
#         print xss
#         print 'lazy:  ', lazy
#         print 'brute: ', brute
#     print '.'
