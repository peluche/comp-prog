import math
 
EPS = 1e-6
 
def step(f, a, b):
    return abs(b - a) / 6.0 * (f(a) + 4.0 * f((a + b) / 2.0) + f(b))
 
def simpson(f, a, b, epsilon, total):
    mid = (a + b) / 2.0
    left = step(f, a, mid)
    right = step(f, mid, b)
    # total = step(f, a, b)
    if abs(left + right - total) <= 15 * epsilon:
        return left + right + (left + right - total) / 15.0
    return simpson(f, a, mid, epsilon / 2.0, left) + simpson(f, mid, b, epsilon / 2.0, right)
 
def solve(nss, qss):
    res = []
    for xx1, y1, xx2, y2 in qss:
        area = 0.0
        for x, y, r in nss:
            left = x - r
            right = x + r
            x1, x2 = xx1, xx2
            if xx1 < left and xx2 > left: x1 = left
            if xx2 > right and xx1 < right: x2 = right
            def f(val):
                if abs(val - x) >= r: return 0
                top = math.sqrt(r**2 - abs(val - x)**2)
                bot = -top
                top += y
                bot += y
                if top > y2: top = y2
                if top < y1: top = y1
                if bot > y2: bot = y2
                if bot < y1: bot = y1
                return top - bot
            
            circle_overlap = simpson(f, x1, x2, EPS, step(f, x1, x2))
            area += circle_overlap
        res.append(area)
    return '\n'.join('{0:.15f}'.format(i) for i in res)
 
if __name__ == '__main__':
    n, q = map(int, raw_input().split())
    nss = [map(int, raw_input().split()) for _ in range(n)]
    qss = [map(int, raw_input().split()) for _ in range(q)]
    print solve(nss, qss)
