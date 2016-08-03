def count_bin_ones(n):
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count

def solve(xs):
    tasks = sorted(xs, key=count_bin_ones)
    return ' '.join(str(task) for task in tasks)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        raw_input()
        print solve(map(int, raw_input().split()))
