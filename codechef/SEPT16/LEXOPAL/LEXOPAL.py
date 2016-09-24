def solve(xs):
    res = []
    for x, y in zip(xs, xs[::-1]):
        if x == '.' and y == '.': res.append('a')
        elif x == '.': res.append(y)
        elif y == '.' or x == y: res.append(x)
        else: return '-1'
    return ''.join(res)
        
if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print solve(raw_input())
