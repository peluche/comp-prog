def solve(xs, ys):
    last = None
    best = 0
    for j, y in reversed(list(enumerate(ys))):
        if y == last: continue
        found = j
        start = 0
        end = len(xs) - 1
        while start <= end:
            mid = (start + end) / 2
            if y < xs[mid]: start = mid + 1
            else:
                found = min(found, mid)
                end = mid - 1
        best = max(best, j - found)
    return best
        
if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _ = raw_input()
        xs = map(int, raw_input().split())
        ys = map(int, raw_input().split())
        print solve(xs, ys)
