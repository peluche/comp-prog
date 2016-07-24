def solve(xs, ys):
    res = []
    i, j = 0, 0
    while True:
        if i >= len(xs):
            res.extend(ys[j:])
            break
        if j >= len(ys) or xs[i] > ys[j]:
            res.append(xs[i])
            i += 1
        else:
            res.append(ys[j])
            j += 1
    return ' '.join(str(r) for r in res)
    
if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _ = raw_input()
        xs = map(int, raw_input().split())
        ys = map(int, raw_input().split())
        print solve(xs, ys)
