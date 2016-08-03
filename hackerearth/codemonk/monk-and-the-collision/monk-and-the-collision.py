def solve(xs):
    buckets = [-1] * 10
    for x in xs:
        buckets[x % 10] += 1
    return sum(max(0, x) for x in buckets)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        raw_input()
        print solve(map(int, raw_input().split()))
