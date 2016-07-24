import heapq

def solve(xss, n, k):
    '''
    use two heaps to select the cheapest k row / col in O(k.log(n))
    select the cheapeast combination of "i rows" + "k-i cols" + i * (k - i)
    '''
    rows = [sum(xs) for xs in xss]
    cols = [sum(xs) for xs in zip(*xss)]
    heapq.heapify(rows)
    heapq.heapify(cols)
    smallest_rows = []
    smallest_cols = []
    for _ in range(k):
        smallest_rows.append(heapq.heapreplace(rows, rows[0] + n))
        smallest_cols.append(heapq.heapreplace(cols, cols[0] + n))
    mini = sum(smallest_rows)
    for i in range(k + 1):
        i_rows = sum(smallest_rows[:i])
        k_i_cols = sum(smallest_cols[:k - i])
        cost = i_rows + k_i_cols + i * (k - i)
        if cost < mini: mini = cost
    return mini

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        n, k = map(int, raw_input().split())
        xss = [map(int, raw_input().split()) for _ in range(n)]
        print solve(xss, n, k)
