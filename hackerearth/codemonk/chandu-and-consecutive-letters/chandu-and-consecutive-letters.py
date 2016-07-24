def solve(xs):
    last = None
    res = []
    for x in xs:
        if x != last:
            last = x
            res.append(x)
    return ''.join(res)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print solve(raw_input())
