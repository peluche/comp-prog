def solve(xs, goal):
    running_sum = 0
    left = 0
    for x in xs:
        running_sum += x
        while running_sum > goal:
            running_sum -= xs[left]
            left += 1
        if running_sum == goal: return 'YES'
    return 'NO'

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        n, goal = map(int, raw_input().split())
        xs = [int(raw_input()) for _ in range(n)]
        print solve(xs, goal)
