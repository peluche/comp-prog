def solve(xs):
    if sum(xs) % 2 == 0: return len(xs)
    i = 0
    while i < len(xs) and xs[i] % 2 == 0 and xs[-i - 1] % 2 == 0:
        i += 1
    return len(xs) - i - 1

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        raw_input()
        print solve(map(int, raw_input().split()))
