def solve(xs):
    return '\n'.join(sorted(set(xs)))

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print solve([raw_input() for _ in range(int(raw_input()))])
