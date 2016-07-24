def is_enlightened(xs, k, power):
    last_position = xs[0] + power
    k -= 1
    for x in xs:
        if x > last_position + power:
            last_position = x + power
            k -= 1
    return k >= 0

def solve(xs, k):
    xs.sort()
    start = 0
    end = (xs[0] + xs[-1]) / 2 + 1
    found = end
    while start <= end:
        mid = (start + end) / 2
        if not is_enlightened(xs, k, mid): start = mid + 1
        else:
            found = mid
            end = mid - 1
    return found

if __name__ == '__main__':
    _, k = map(int, raw_input().split())
    xs = map(int, raw_input().split())
    print solve(xs, k)
