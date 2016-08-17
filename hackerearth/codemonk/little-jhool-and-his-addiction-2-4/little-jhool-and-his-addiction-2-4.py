def solve(xs, k):
    xs.sort()
    pairs = [x + y for x, y in zip(xs[:len(xs) / 2], xs[len(xs) / 2:][::-1])]
    diff = max(pairs) - min(pairs)
    if diff < k: res = "Chick magnet Jhool!"
    elif diff == k: res = "Lucky chap!"
    else: res = "No more girlfriends!"
    return '{}\n{}'.format(diff, res)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _, k = map(int, raw_input().split())
        xs = map(int, raw_input().split())
        print solve(xs, k)
