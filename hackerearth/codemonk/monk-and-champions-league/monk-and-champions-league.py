import heapq

def solve(n, xs):
    xs = [-x for x in xs]
    heapq.heapify(xs)
    tot = 0
    for _ in range(n):
        price = xs[0]
        tot += price
        heapq.heapreplace(xs, price + 1)
    return -tot

if __name__ == '__main__':
    _, n = map(int, raw_input().split())
    xs = map(int, raw_input().split())
    print solve(n, xs)
