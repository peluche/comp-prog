def count_1(x):
    count = 0
    while x:
        x &= x - 1
        count += 1
    return count
    
def solve(xs, k):
    return sum(sorted(map(count_1, xs), reverse=True)[:k])

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _, k = map(int, raw_input().split())
        xs = map(int, raw_input().split())
        print solve(xs, k)
