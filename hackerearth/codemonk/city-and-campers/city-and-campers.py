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
    group_sizes = [1] * n
    count_group_of_size = [0] * (n + 1)
    count_group_of_size[1] = n
    smaller_index = 1
    maxi = 1
    res = []
    for a, b in xss:
        root_a = find(parents, a - 1)
        root_b = find(parents, b - 1)
        if root_a != root_b:
            union(parents, depths, root_a, root_b)
            count_group_of_size[group_sizes[root_a]] -= 1
            count_group_of_size[group_sizes[root_b]] -= 1
            new_size = group_sizes[root_a] + group_sizes[root_b]
            group_sizes[root_a] = new_size
            group_sizes[root_b] = new_size
            count_group_of_size[new_size] += 1
            maxi = max(maxi, new_size)
            while count_group_of_size[smaller_index] == 0: smaller_index += 1
        res.append(str(maxi - smaller_index))
    return '\n'.join(res)

if __name__ == '__main__':
    n, q = map(int, raw_input().split())
    xss = [map(int, raw_input().split()) for _ in range(q)]
    print solve(n, xss)
