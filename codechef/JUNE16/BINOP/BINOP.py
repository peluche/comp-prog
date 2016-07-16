import collections

luck = 'Lucky Chef\n{}'
no_luck = 'Unlucky Chef'

def solve(xs, ys):
    if len(collections.Counter(xs)) == 1 and xs != ys:
        return no_luck
    diff_1, diff_2 = 0, 0
    for x, y in zip(xs, ys):
        if x != y:
            if x == '1': diff_1 += 1
            else: diff_2 += 1
    return luck.format(max(diff_1, diff_2))
    
if __name__ == '__main__':
    for _ in range(int(raw_input())):
        A = raw_input()
        B = raw_input()
        res = solve(A, B)
        print '{}'.format(res)
