import bisect
    
def solve(xs, k):
    start = 0
    end = len(xs) - k
    res = []
    pos = [[] for _ in range(ord('z') - ord('a') + 1)]
    for i in range(end + 1):
        pos[ord(xs[i]) - ord('a')].append(i)
        
    for _ in range(k): # pick k letters
        for i in range(ord('z') - ord('a') + 1): # greedily
            x = bisect.bisect_left(pos[i], start)
            if x < len(pos[i]):
                start = pos[i][x]
                pos[i][x] = -1
                res.append(xs[start])
                break

        # increate the window
        end += 1
        if end < len(xs):
            pos[ord(xs[end]) - ord('a')].append(end)

    return ''.join(res)
        
if __name__ == "__main__":
    for _ in range(int(raw_input())):
        XS = raw_input()
        K = int(raw_input())
        res = solve(XS, K)
        print "{}".format(res)
