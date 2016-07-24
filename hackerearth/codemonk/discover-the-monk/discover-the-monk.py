def solve(xs, qs):
    els = set(xs)
    return '\n'.join('YES' if q in els else 'NO' for q in qs)

if __name__ == '__main__':
    _, q = map(int, raw_input().split())
    xs = map(int, raw_input().split())
    qs = [int(raw_input()) for _ in range(q)]
    print solve(xs, qs)
