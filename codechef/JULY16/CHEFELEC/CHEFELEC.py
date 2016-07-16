import heapq

def add_village(xs, es, h, i):
    es[i] = 1
    if i > 0 and not es[i - 1]:
        heapq.heappush(h, (xs[i] - xs[i - 1], i - 1))
    if i + 1 < len(es) and not es[i + 1]:
        heapq.heappush(h, (xs[i + 1] - xs[i], i + 1))
        
def solve(es, xs):
    h = []
    for i, e in enumerate(es):
        if e: add_village(xs, es, h, i)
    cost = 0
    while h:
        val, village = heapq.heappop(h)
        if not es[village]:
            cost += val
            add_village(xs, es, h, village)
    return cost
    
if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _ = int(raw_input())
        ES = [int(x) for x in raw_input()]
        XS = map(int, raw_input().split())
        res = solve(ES, XS)
        print '{}'.format(res)
