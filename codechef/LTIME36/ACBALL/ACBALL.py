def solve(xs, ys):
    opposite = {'W': 'B', 'B': 'W'}
    pairs = zip(xs, ys)
    res = []
    for x, y in pairs:
        if x == y: res.append(opposite[x])
        else: res.append('B')
    return ''.join(res)
    
if __name__ == "__main__":
    for t in range(int(raw_input())):
        XS = raw_input()
        YS = raw_input()
        res = solve(XS, YS)
        print "{}".format(res)
