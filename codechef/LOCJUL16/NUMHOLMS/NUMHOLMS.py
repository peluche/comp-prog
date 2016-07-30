import collections

def remove1mod(count):
    if 1 in count and count[1] > 0: count[1] -= 1
    elif 4 in count and count[4] > 0: count[4] -= 1
    elif 7 in count and count[7] > 0: count[7] -= 1
    else: return False
    return True

def remove2mod(count):
    if 2 in count and count[2] > 0: count[2] -= 1
    elif 5 in count and count[5] > 0: count[5] -= 1
    elif 8 in count and count[8] > 0: count[8] -= 1
    else: return False
    return True

def solve(xs):
    if 0 not in xs: return -1
    count = collections.Counter(xs)
    s = sum(k * v for k, v in count.items())
    if s % 3 == 1:
        if not remove1mod(count):
            remove2mod(count)
            remove2mod(count)
    elif s % 3 == 2:
        if not remove2mod(count):
            remove1mod(count)
            remove1mod(count)
    s = sum(k * v for k, v in count.items())
    if s % 3 != 0: return -1
    elif s == 0: return 0
    return ''.join(str(k) * count[k] for k in sorted(count.keys(), reverse=True))

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        raw_input()
        print solve(map(int, raw_input().split()))
