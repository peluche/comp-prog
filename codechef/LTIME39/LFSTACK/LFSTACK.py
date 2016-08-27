import sys
sys.setrecursionlimit(10**7)

def update(inds, up):
    return inds[:up] + ((inds[up] - 1),) + inds[up + 1:]

def rec(xs, xss, ind, inds, mem):
    if ind == len(xs): return True
    if inds in mem: return mem[inds]
    
    target = xs[ind]
    for up, i, x in zip(range(len(inds)), inds, xss):
        if i == -1: continue
        if x[i] == target and rec(xs, xss, ind + 1, update(inds, up), mem):
            mem[inds] = True
            return True
    mem[inds] = False
    return False

def solve(xss, xs):
    if len(xss) == 1: return 'Yes' if list(reversed(xss[0])) == xs else 'No'
    return 'Yes' if rec(xs, xss, 0, tuple([len(x) - 1 for x in xss]), {}) else 'No'

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        n = int(raw_input())
        xss = [map(int, raw_input().split()[1:]) for _ in range(n)]
        xs = map(int, raw_input().split())
        print solve(xss, xs)
