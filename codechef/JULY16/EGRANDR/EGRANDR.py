def solve(xs):
    if min(xs) > 2 and max(xs) == 5 and sum(xs) / len(xs) >= 4:
        return "Yes"
    return "No"

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _ = int(raw_input())
        XS = map(int, raw_input().split())
        res = solve(XS)
        print '{}'.format(res)
