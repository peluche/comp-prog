def solve(word, reserve):
    i = 0
    reserve = sorted(list(reserve))
    res = []
    for c in word:
        if i < len(reserve) and reserve[i] < c:
            res.append(reserve[i])
            i += 1
        else: res.append(c)
    return ''.join(res)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        w = raw_input()
        r = raw_input()
        print solve(w, r)
