def solve(xs):
    return '\n'.join('{} {}'.format(*x) for x in sorted(xs, key=lambda x: (-int(x[1]), x[0])))

if __name__ == '__main__':
    print solve([raw_input().split() for _ in range(int(raw_input()))])
