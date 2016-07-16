BASE = '02468'

def to_base_5_ish(kth):
    if kth == 0: return BASE[0]
    res = []
    while kth:
        res.append(BASE[kth % len(BASE)])
        kth /= len(BASE)
    return ''.join(reversed(res))

def solve(k):
    return to_base_5_ish(k - 1)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        K = int(raw_input())
        res = solve(K)
        print '{}'.format(res)
