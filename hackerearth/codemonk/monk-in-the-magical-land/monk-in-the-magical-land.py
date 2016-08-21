def gcd(a, b):
    if not b: return a
    return gcd(b, a % b)

def memo(f):
    mem = {}
    def ret(keys_to_chest, booty, opened):
        k = (id(keys_to_chest), opened)
        if k not in mem: mem[k] = f(keys_to_chest, booty, opened)
        return mem[k]
    return ret

@memo
def score(keys_to_chest, booty, opened):
    i = 0
    reward = 0
    while opened:
        if opened & 1: reward += booty[i]
        i += 1
        opened /= 2
    return reward

def pick_k(keys_to_chest, booty, k, starting_at=0, opened=0):
    if k == 0: return score(keys_to_chest, booty, opened)
    best_booty = 0
    for key in range(starting_at, len(keys_to_chest)):
        val = max(best_booty, pick_k(keys_to_chest, booty, k - 1, key + 1, opened | keys_to_chest[key]))
        if val > best_booty: best_booty = val
    return best_booty

def solve(k, ns, cs, zs):
    keys_to_chest = [sum(1 << i for i, c in enumerate(cs) if gcd(c, key) != 1) for key in ns]
    return pick_k(keys_to_chest, zs, k)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        n, m, k = map(int, raw_input().split())
        ns = map(int, raw_input().split())
        cs = map(int, raw_input().split())
        zs = map(int, raw_input().split())
        print solve(k, ns, cs, zs)
