import heapq

def distances(xss, k, start):
    h = [start]
    dist = [[-1] * len(xss[0]) for _ in range(len(xss))]
    dist[start[1]][start[2]] = start[0]
    
    while h:
        val, x, y = heapq.heappop(h)
        for i in range(k + 1):
            for j in range(k + 1 - i):
                for io in (-1, 1):
                    for jo in (-1, 1):
                        ii = x + i * io
                        jj = y + j * jo
                        if ii >= 0 and ii < len(xss) and jj >= 0 and jj < len(xss[0]) and dist[ii][jj] == -1 and xss[ii][jj] == 0:
                            dist[ii][jj] = val + 1
                            heapq.heappush(h, (val + 1, ii, jj))
    return dist
    
def solve(xss, k1, k2):
    d1 = distances(xss, k1, (0, 0, 0))
    d2 = distances(xss, k2, (0, 0, len(xss[0]) - 1))
    found = False
    mini = float('inf')
    for i in range(len(xss)):
        for j in range(len(xss[0])):
            if d1[i][j] != -1 and d2[i][j] != -1:
                found += 1
                mini = min(mini, max(d1[i][j], d2[i][j]))
    if found: return mini
    return -1
                                           
if __name__ == '__main__':
    for _ in range(int(raw_input())):
        N, M, K1, K2 = map(int, raw_input().split())
        xss = []
        for _ in range(N):
            xss.append(map(int, raw_input().split()))
        res = solve(xss, K1, K2)
        print '{}'.format(res)
