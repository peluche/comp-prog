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

def solve(n, xss):
    depths = [1] * n
    parents = range(0, n)
    for i, j in xss:
        union(parents, depths, find(parents, i - 1), find(parents, j - 1))
    for i in range(n):
        find(parents, i)
    return len(set(parents))

if __name__ == '__main__':
    ''' The input files on codemonk are hill formatted wtf ... '''
    malformed_input = raw_input()
    if ' ' in malformed_input:
        n, k = map(int, malformed_input.split())
    else:
        n = int(malformed_input)
        k = int(raw_input())
    xss = [map(int, raw_input().split()) for _ in range(k)] 
    print solve(n, xss)
