import heapq

def solve(k, xs):
    ys = [-x for x in xs]
    heapq.heapify(ys)
    count = 0
    for _ in range(k):
        count += -ys[0]
        heapq.heapreplace(ys, -((-ys[0]) / 2))
    return count

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _, k = map(int, raw_input().split())
        xs = map(int, raw_input().split())
        print solve(k, xs)
