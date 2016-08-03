import collections

MOD = 1000000007

def union(parents, depths, i, j):
    ''' Union with under the deepest root '''
    if depths[i] > depths[j]:
        parents[j] = i
    else:
        parents[i] = j
        depths[i] = max(depths[i], depths[j] + 1)

def find(parents, el):
    ''' Find an element and compress the sets '''
    if parents[el] == el: return el
    leader = find(parents, parents[el])
    parents[el] = leader
    return leader

def solve(risks, roads):
    depths = [1] * len(risks)
    parents = range(0, len(risks))
    for a, b in roads:
        union(parents, depths, find(parents, a - 1), find(parents, b - 1))

    clusters_min_count = collections.defaultdict(lambda: [float('inf'), 0])
    for city in range(0, len(risks)):
        root = find(parents, city)
        if risks[city] < clusters_min_count[root][0]:
            clusters_min_count[root] = [risks[city], 1]
        elif risks[city] == clusters_min_count[root][0]:
            clusters_min_count[root][1] += 1
    count = 1
    for _, nb in clusters_min_count.values():
        count = (count * nb) % MOD
    return count

if __name__ == '__main__':
    raw_input()
    xs = map(int, raw_input().split())
    xss = [map(int, raw_input().split()) for _ in range(int(raw_input()))]
    print solve(xs, xss)
