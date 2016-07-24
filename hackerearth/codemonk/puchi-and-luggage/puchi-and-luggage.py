def merge_sort_count(xss):
    if len(xss) == 1:
        return xss
    mid = len(xss) / 2
    xs = merge_sort_count(xss[:mid])
    ys = merge_sort_count(xss[mid:])
    res = []
    i, j, count = 0, 0, 0
    while True:
        if i >= len(xs):
            res.extend(ys[j:])
            break
        if j >= len(ys) or xs[i] < ys[j]:
            res.append((xs[i][0], xs[i][1] + count))
            i += 1
        else:
            count += 1
            res.append(ys[j])
            j += 1
    return res

def solve(xs):
    lookup = dict(merge_sort_count(zip(xs, [0] * len(xs))))
    res = []
    for x in xs:
        res.append(str(lookup[x]))
    return ' '.join(res)
    
if __name__ == '__main__':
    for _ in range(int(raw_input())):
        n = int(raw_input())
        xs = [int(raw_input()) for _ in range(n)]
        print solve(xs)
