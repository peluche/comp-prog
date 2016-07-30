def solve(n, m, xs):
    '''
    The subject is anbiguous:
    - students can sit in group of more than 2
    - even if a student can't be paired he stills enter the class-room
    '''
    res = []
    s = set(xs[:n])
    for x in xs[n:]:
        res.append('YES' if x in s else 'NO')
        s.add(x)
    return '\n'.join(res)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        n, m = map(int, raw_input().split())
        xs = map(int, raw_input().split())
        print solve(n, m, xs)
