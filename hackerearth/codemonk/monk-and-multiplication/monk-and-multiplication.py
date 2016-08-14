def prod(xs):
    p = 1
    for x in xs:
        p *= x
    return p

def solve(xs):
    res = []
    biggests = []
    for x in xs:
        biggests.append(x)
        biggests.sort(reverse=True)
        while len(biggests) > 3: biggests.pop()
        res.append(prod(biggests) if len(biggests) == 3 else -1)
    return '\n'.join(str(x) for x in res)

if __name__ == '__main__':
    raw_input()
    print solve(map(int, raw_input().split()))
