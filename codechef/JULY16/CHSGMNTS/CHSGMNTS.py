import collections
import bisect

def occurences(xs):
    occ = collections.defaultdict(list)
    for i, x in enumerate(xs):
        occ[x].append(i)
    return occ

def merge_in(els, occs, idx):
    """ for some reason sorted() is faster than heapq.merge() """
    i = bisect.bisect_left(els, idx)
    j = bisect.bisect_left(occs, idx)
    return sorted(els[i:] + occs[j:])
    
def count_intervals(els, idx, size):
    count = 0
    start = idx
    for end in els:
        if end < start: continue
        n = end - start - 1
        count += n * (n + 1) / 2
        start = end
    n = size - start - 1
    count += n * (n + 1) / 2
    return count
        
def solve(xs):
    size = len(xs)
    occ = occurences(xs)
    count = 0
    for a in range(size):
        seen = set()
        els = []
        for b in range(a, size):
            if xs[b] not in seen:
                seen.add(xs[b])
                els = merge_in(els, occ[xs[b]], b)
                last = count_intervals(els, b, size)
            count += last
    return count

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _ = raw_input()
        xs = map(int, raw_input().split())
        res = solve(xs)
        print '{}'.format(res)

# def bench():
#     import sys
#     import random
#     xs = [random.randrange(10) for _ in range(int(sys.argv[1]))]
#     print solve2(xs)
#     assert solve(xs) == solve2(xs)

# bench()
