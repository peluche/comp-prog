import collections

def solve(xs):
    c = collections.Counter(xs)
    return "Yes" if 1 in c.values() else "No"

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print solve(raw_input())
