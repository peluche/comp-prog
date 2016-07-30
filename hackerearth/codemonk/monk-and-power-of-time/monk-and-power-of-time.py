import collections

def solve(xs, ys):
    q = collections.deque(xs)
    i = 0
    count = 0
    while len(q):
        el = q.popleft()
        if el != ys[i]: q.append(el)
        else: i += 1
        count += 1
    return count

if __name__ == '__main__':
    raw_input()
    print solve(map(int, raw_input().split()), map(int, raw_input().split()))
