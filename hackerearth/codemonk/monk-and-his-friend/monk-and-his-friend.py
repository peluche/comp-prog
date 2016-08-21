def solve(n, m):
    count = 0
    x = n ^ m
    while x:
        x &= x - 1
        count += 1
    return count

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        n, m = map(int, raw_input().split())
        print solve(n, m)
