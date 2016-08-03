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

class Node:
    start = None
    end = None
    left = None
    right = None
    leftmost_val = None
    rightmost_val = None
    min_interval = None
    count = 0
    
def make_empty_interval_tree(start, end):
    node = Node()
    node.start = start
    node.end = end
    if start == end:
        node.count = 0
        return node
    mid = (start + end) / 2
    node.left = make_empty_interval_tree(start, mid)
    node.right = make_empty_interval_tree(mid + 1, end)
    return node

def update_node(root, pos, delta):
    if pos == root.start and pos == root.end:
        root.count += delta
        root.min_interval = None
        root.leftmost_val = root.start
        root.rightmost_val = root.start
        if root.count == 0:
            root.leftmost_val = None
            root.rightmost_val = None
            return
        if root.count > 1:
            root.min_interval = 0
        return
    if pos <= root.left.end: update_node(root.left, pos, delta)
    else: update_node(root.right, pos, delta)
    # index from 1 or it will break :p
    root.leftmost_val = root.left.leftmost_val or root.left.rightmost_val or root.right.leftmost_val or root.right.rightmost_val
    root.rightmost_val = root.right.rightmost_val or root.right.leftmost_val or root.left.rightmost_val or root.left.leftmost_val

    mini = []
    if root.left.min_interval != None: mini.append(root.left.min_interval)
    if root.right.min_interval != None: mini.append(root.right.min_interval)
    if root.left.rightmost_val and root.right.leftmost_val: mini.append(root.right.leftmost_val - root.left.rightmost_val)
    root.min_interval = min(mini) if mini else None
    
def solve(n, xss):
    itree = make_empty_interval_tree(1, n)
    update_node(itree, 1, n)
    depths = [1] * n
    parents = range(0, n)
    group_sizes = [1] * n
    res = []
    for a, b in xss:
        root_a = find(parents, a - 1)
        root_b = find(parents, b - 1)
        if root_a != root_b:
            union(parents, depths, root_a, root_b)
            s1 = group_sizes[root_a]
            s2 = group_sizes[root_b]
            new_size = s1 + s2
            group_sizes[root_a] = new_size
            group_sizes[root_b] = new_size
            update_node(itree, s1, -1)
            update_node(itree, s2, -1)
            update_node(itree, new_size, 1)
        res.append(str(itree.min_interval or 0))
    return '\n'.join(res)

if __name__ == '__main__':
    n, q = map(int, raw_input().split())
    xss = [map(int, raw_input().split()) for _ in range(q)]
    print solve(n, xss)
