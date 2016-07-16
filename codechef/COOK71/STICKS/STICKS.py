import collections

def solve(xs):
    count = collections.Counter(xs)
    vals = []
    for k, v in count.items():
        if v >= 4:
            vals.append(k)
        if v >= 2:
            vals.append(k)
    vals.sort(reverse=True)
    if len(vals) < 2: return -1
    return vals[0] * vals[1]

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _ = raw_input()
        XS = map(int, raw_input().split())
        res = solve(XS)
        print '{}'.format(res)
