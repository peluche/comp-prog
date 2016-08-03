def union(parents, i, j):
    ''' Union with under the deepest root '''
    parents[i] = j

def find(parents, el):
    ''' Find an element and compress the sets '''
    if parents[el] == el: return el
    leader = find(parents, parents[el])
    parents[el] = leader
    return leader

def solve(n, xss):
    res = []
    parents = range(0, n)
    for xs in xss:
        if xs[0] == 1:
            root_a = find(parents, xs[1] - 1)
            root_b = find(parents, xs[2] - 1)
            if root_a == root_b: continue
            union(parents, root_a, root_b)
        elif xs[0] == 2:
            el = xs[1] - 1
            root_a = find(parents, el)
            parents[root_a] = el
            parents[el] = el
        else:
            res.append(str(find(parents, xs[1] - 1) + 1))
    return '\n'.join(res)

if __name__ == '__main__':
    n, q = map(int, raw_input().split())
    xss = [map(int, raw_input().split()) for _ in range(q)]
    print solve(n, xss)
