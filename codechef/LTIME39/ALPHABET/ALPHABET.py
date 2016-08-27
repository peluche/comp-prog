import collections

def solve(s, xs):
    d = collections.defaultdict(lambda: False)
    for c in s: d[c] = True
    res = []
    for x in xs:
        res.append("Yes" if all(d[c] for c in x) else "No")
    return '\n'.join(res)

if __name__ == '__main__':
    s = raw_input()
    n = int(raw_input())
    xs = [raw_input() for _ in range(n)]
    print solve(s, xs)
