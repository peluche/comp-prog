import collections

def solve(xs):
    couples = collections.defaultdict(lambda: [0, 0])
    for x in xs:
        if x[-2:] == 'ki': couples[x[:-2]][0] += 1
        if x[-2:] == 'ka': couples[x[:-2]][1] += 1
    return sum(min(v) for v in couples.values())

if __name__ == '__main__':
    raw_input()
    print solve(raw_input().split())
