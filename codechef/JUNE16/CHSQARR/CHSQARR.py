import math
import copy

# def pre_process_max_ranges(xss, rows, cols):
#     res = [[[[0 for ri in range(int(math.log(rows, 2)) + 2)] for ci in range(int(math.log(cols, 2)) + 2)] for c in range(cols)] for r in range(rows)]
#     for r in range(rows):
#         for c in range(cols):
#             res[r][c][0][0] = xss[r][c]

#     for r in range(rows):
#         for ci in range(1, cols + 1):
#             if (1 << ci) > cols: break
        
#             for c in range(cols):
#                 if c + (1 << ci) - 1 >= cols: break

#                 left = res[r][c][ci - 1][0]
#                 right = res[r][c + (1 << (ci - 1))][ci - 1][0]
#                 res[r][c][ci][0] = max(left, right)

#     for ri in range(1, rows + 1):
#         if (1 << ri) > rows: break

#         for r in range(rows):
#             if r + (1 << ri) - 1 >= rows: break

#             for ci in range(0, cols + 1):
#                 if (1 << ci) > cols: break
        
#                 for c in range(cols):
#                     if c + (1 << ci) - 1 >= cols: break

#                     left =  res[r][c][ci][ri - 1]
#                     right = res[r + (1 << (ri - 1))][c][ci][ri - 1]
#                     res[r][c][ci][ri] = max(left, right)
#     return res

AA = None
BB = None
CC = None

def init_maxes(size):
    return [0] * size

def pre_process_max_ranges(xss, rows, cols):
    '''
    python is slow
    replace: maxi = max(maxi, element)
    by:      maxi = maxi if maxi > element else element

    using nested python list is awfully slow,
    having a huge list and doing the offset math by hand is way faster
    replace: res[a][b][c] = ...
    by:      res[a * A + b * B + c]
    '''
    global AA
    global BB
    global CC

    log_rows = int(math.log(rows, 2)) + 2
    log_cols = int(math.log(cols, 2)) + 2
    
    AA = cols * log_cols * log_rows
    BB = log_cols * log_rows
    CC = log_rows

    res = init_maxes(rows * cols * log_cols * log_rows)
    for r in range(rows):
        for c in range(cols):
            res[r * AA + c * BB] = xss[r][c]
            # res[r][c][0][0] = xss[r][c]

    for r in range(rows):
        for ci in range(1, cols + 1):
            if (1 << ci) > cols: break
        
            for c in range(cols):
                if c + (1 << ci) - 1 >= cols: break

                left = res[r * AA + c * BB + (ci - 1) * CC]
                # left = res[r][c][ci - 1][0]
                right = res[r * AA + (c + (1 << (ci - 1))) * BB + (ci - 1) * CC]
                # right = res[r][c + (1 << (ci - 1))][ci - 1][0]
                # res[r * AA + c * BB + ci * CC] = max(left, right)
                # # res[r][c][ci][0] = max(left, right)
                # XXX
                if left > right: res[r * AA + c * BB + ci * CC] = left
                else: res[r * AA + c * BB + ci * CC] = right


    for ri in range(1, rows + 1):
        if (1 << ri) > rows: break

        for r in range(rows):
            if r + (1 << ri) - 1 >= rows: break

            for ci in range(0, cols + 1):
                if (1 << ci) > cols: break
        
                for c in range(cols):
                    if c + (1 << ci) - 1 >= cols: break

                    left =  res[r * AA + c * BB + ci * CC + ri - 1]
                    # left =  res[r][c][ci][ri - 1]
                    right = res[(r + (1 << (ri - 1))) * AA + c * BB + ci * CC + ri - 1]
                    # right = res[r + (1 << (ri - 1))][c][ci][ri - 1]
                    # res[r * AA + c * BB + ci * CC + ri] = max(left, right)
                    # # res[r][c][ci][ri] = max(left, right)
                    # XXX
                    if left > right: res[r * AA + c * BB + ci * CC + ri] = left
                    else: res[r * AA + c * BB + ci * CC + ri] = right
    return res

def max_range(res, r, c, ci):
    k = int(math.log(ci - c + 1, 2))
    left = res[(r, c, k, 0)]
    right = res[(r, ci - (2**k) + 1, k, 0)]
    return max(left, right)

def max_rect(res, r, c, ci, ri):
    k = int(math.log(ci - c + 1, 2))
    l = int(math.log(ri - r + 1, 2))
    return max(
        res[r * AA + c * BB + k * CC + l],
        # res[r][c][k][l],
        res[r * AA + (ci - (2**k) + 1) * BB + k * CC + l],
        # res[r][ci - (2**k) + 1][k][l],
        res[(ri - (2**l) + 1) * AA + c * BB + k * CC + l],
        # res[ri - (2**l) + 1][c][k][l],
        res[(ri - (2**l) + 1) * AA + (ci - (2**k) + 1) * BB + k * CC + l]
        # res[ri - (2**l) + 1][ci - (2**k) + 1][k][l]
    )

def brute_max(xss, r, c, ci):
    maxi = 0
    for x in range(c, ci + 1):
        maxi = max(maxi, xss[r][x])
    return maxi

def brute_max_rect(xss, r, c, ci, ri):
    maxi = 0
    for y in range(r, ri + 1):
        for x in range(c, ci + 1):
            maxi = max(maxi, xss[y][x])
    return maxi

def test_preprocess_max(rows=1000, cols=500):
    import random
    test = [[random.randrange(100) for _ in range(cols)] for _ in range(rows)]
    print 'start preprocess'
    res = pre_process_max_ranges(test, rows, cols)
    print 'end preprocess'

def test_rect(rows=50, cols=70):
    import random
    test = [[random.randrange(100) for _ in range(cols)] for _ in range(rows)]
    res = pre_process_max_ranges(test, rows, cols)
    
    for r in range(rows):
        for c in range(cols):
            for ci in range(c, cols):
                for ri in range(r, rows):
                    s1 = max_rect(res, r, c, ci, ri)
                    s2 = brute_max_rect(test, r, c, ci, ri)
                    assert s1 == s2, 'test {}\nr: {} | c: {} | ci: {} | ri: {} | s1: {} | s2: {}'.format(test, r, c, ci, ri, s1, s2)
    print '[.] test_rect'


def test_rows(rows=50, cols=70):
    import random
    test = [[random.randrange(100) for _ in range(cols)] for _ in range(rows)]
    res = pre_process_max_ranges(test, rows, cols)

    for r in range(rows):
        for c in range(cols):
            for ci in range(c, cols):
                s1 = max_range(res, r, c, ci)
                s2 = brute_max(test, r, c, ci)
                assert s1 == s2, 'test {}\nr: {} | c: {} | ci: {} | s1: {} | s2: {}'.format(test, r, c, ci, s1, s2)
    print '[.] test_rows'

def preprocess_sum_rect(xss, rows, cols):
    sums = copy.deepcopy(xss)
    for c in range(1, cols):
        sums[0][c] += sums[0][c - 1]

    for r in range(1, rows):
        sums[r][0] += sums[r - 1][0]
    
    for r in range(1, rows):
        for c in range(1, cols):
            sums[r][c] += sums[r - 1][c] + sums[r][c - 1] - sums[r - 1][c - 1]

    return sums

def sum_rect(sums, r, c, ci, ri):
    r -= 1
    c -= 1
    total = sums[ri][ci]
    if r >= 0: total -= sums[r][ci]
    if c >= 0: total -= sums[ri][c]
    if r >= 0 and c >= 0: total += sums[r][c]
    return total

def brute_sum_rect(xss, r, c, ci, ri):
    total = 0
    for x in range(r, ri + 1):
        for y in range(c, ci + 1):
            total += xss[x][y]
    return total

def test_sum_rect(rows=50, cols=70):
    import random
    test = [[random.randrange(100) for _ in range(cols)] for _ in range(rows)]
    sums = preprocess_sum_rect(test, rows, cols)
    things = '\n'.join(['{}'.format(x) for x in test]) + '\n\n' + '\n'.join(['{}'.format(x) for x in sums])
    
    for r in range(rows):
        for c in range(cols):
            for ci in range(c, cols):
                for ri in range(r, rows):
                    s1 = sum_rect(sums, r, c, ci, ri)
                    s2 = brute_sum_rect(test, r, c, ci, ri)
                    assert s1 == s2, 'test {}\nr: {} | c: {} | ci: {} | ri: {} | s1: {} | s2: {}\n{}'.format(test, r, c, ci, ri, s1, s2, things)
    print '[.] test_rect'
    
def test_preprocess_sum(rows=4, cols=5):
    import random
    test = [[random.randrange(10) for _ in range(cols)] for _ in range(rows)]
    sums = preprocess_sum_rect(test, rows, cols)
    print '\n'.join(['{}'.format(x) for x in test])
    print ''
    print '\n'.join(['{}'.format(x) for x in sums])

def bench(n):
    import random
    from timeit import default_timer as timer
    xs = [[random.randrange(100) for _ in range(n)] for _ in range(n)]
    start = timer()
    maxes = pre_process_max_ranges(xs, n, n)
    end = timer()
    print 'maxes: {}'.format(end - start)
    start = timer()
    
    sums = preprocess_sum_rect(xs, n, n)
    end = timer()
    print 'sums: {}'.format(end - start)
    start = timer()

    res = solve(maxes, sums, n/2, n/2, n, n)
    end = timer()
    print 'solve: {}'.format(end - start)

    print '{}'.format(res)

# test_preprocess_max()
# test_rows()
# test_rect()
# test_preprocess_sum()
# test_sum_rect()
# import sys
# bench(int(sys.argv[1]))

def solve(maxes, sums, a, b, rows, cols):
    square = a * b
    mini = float('inf')
    for r in range(rows - a + 1):
        ri = r + a - 1
        for c in range(cols - b + 1):
            ci = c + b - 1
            maxi = max_rect(maxes, r, c, ci, ri)
            sumi = sum_rect(sums, r, c, ci, ri)
            mini = min(mini, maxi * square - sumi)
    return mini

if __name__ == '__main__':
    N, M = map(int, raw_input().split())
    xs = []
    for _ in range(N):
        xs.append(map(int, raw_input().split()))
    maxes = pre_process_max_ranges(xs, N, M)
    sums = preprocess_sum_rect(xs, N, M)
    for _ in range(int(raw_input())):
        A, B = map(int, raw_input().split())
        res = solve(maxes, sums, A, B, N, M)
        print '{}'.format(res)

# import sys
# import cProfile
# cProfile.run('bench(int(sys.argv[1]))')
