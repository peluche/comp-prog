def get_start(colored):
    for node, color in enumerate(colored):
        if color == 0: return node
    return None

def is_2_colorable(g):
    ''' check if the graph is 2 colorable / bipartite '''
    alternate_color = [-1, 2, 1]
    colored = [0] * len(g)
    while True:
        start = get_start(colored)
        if start == None: return True
        color = 1
        layer = {start}
        while layer:
            next_layer = set()
            for node in layer:
                if colored[node] == alternate_color[color]: return False
                if colored[node] == 0:
                    for neighbour, val in enumerate(g[node]):
                        if val: next_layer.add(neighbour)
                colored[node] = color
            layer = next_layer
            color = alternate_color[color]

def to_inverse_graph(xss, n):
    g = [[1] * n for _ in range(n)]
    for i in range(n): g[i][i] = 0
    for a, b in xss:
        g[a - 1][b - 1] = 0
        g[b - 1][a - 1] = 0
    return g

def solve(n, xss):
    g = to_inverse_graph(xss, n)
    return "YES" if is_2_colorable(g) else "NO"

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        n, m = map(int, raw_input().split())
        xss = [map(int, raw_input().split()) for _ in range(m)]
        print solve(n, xss)
