if __name__ == "__main__":
    _, Q = map(int, raw_input().split())
    xs = map(int, raw_input().split())
    mini = min(xs)
    maxi = max(xs)
    for t in range(Q):
        t = int(raw_input())
        res = 'Yes' if mini <= t <= maxi else 'No'
        print "{}".format(res)
