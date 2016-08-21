def solve(mem, ns, ps, pos=0, old2=-1, old1=-1, used=0):
    if pos == len(ps): return 0
    key = (old2, old1, used)
    if key in mem: return mem[key]

    mini = float('inf')
    for i, n in enumerate(ns):
        if used & (1 << i): continue
        val = solve(mem, ns, ps, pos + 1, old1, n, used | (1 << i))
        if old2 >= 0: val += (old2 ^ old1 ^ n) * ps[pos]
        if val < mini: mini = val
    mem[key] = mini
    return mini

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        raw_input()
        ns = map(int, raw_input().split())
        ps = map(int, raw_input().split())
        print solve({}, ns, ps)
