if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _ = raw_input()
        xs = map(int, raw_input().split())
        print ' '.join(str(x) for x in sorted(xs, reverse=True))
