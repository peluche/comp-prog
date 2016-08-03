def solve(xs):
    return 'Yes' if sum(xs) / 2 == len(xs) - 1 else 'No'

if __name__ == '__main__':
    raw_input()
    print solve(map(int, raw_input().split()))
