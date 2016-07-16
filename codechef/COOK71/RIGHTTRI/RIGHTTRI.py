import math
import fractions

def max_area(h):
    return fractions.Fraction(h * h, 4)

def solve(h, s):
    if fractions.Fraction(s) > max_area(h): return -1
    hh = h * h
    start = 0
    end = math.sqrt(hh / 2.0)
    while True:
        mid = (start + end) / 2.0
        b = math.sqrt(hh - mid**2)
        area = mid * b / 2.0
        diff = s - area
        if abs(diff) < 0.00005:
            return '{:f} {:f} {:f}'.format(mid, b, h)
        if area > s:
            end = mid
        else:
            start = mid
    
if __name__ == '__main__':
    for _ in range(int(raw_input())):
        H, S = map(int, raw_input().split())
        res = solve(H, S)
        print '{}'.format(res)

