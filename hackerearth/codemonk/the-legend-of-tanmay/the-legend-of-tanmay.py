def prod(xs):
    p = 1
    for x in xs:
        p *= x
    return p

def solve(xs):
    negatives = sorted(x for x in xs if x < 0)
    positives = sorted(x for x in xs if x > 0)
    zeros = [0] if 0 in xs else []
    if len(negatives) % 2 == 0: maxi = negatives + positives
    else: maxi = negatives[:-1] + positives
    if not maxi and zeros : maxi = zeros
    elif not maxi: maxi = negatives[-1:]

    if len(negatives) % 2 == 1: mini = negatives + positives
    elif len(negatives) >= 2: mini = negatives[:-1] + positives
    else: mini = (zeros + positives)[:1]
    return '{} {}'.format(prod(maxi), prod(mini))

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        raw_input()
        print solve(map(int, raw_input().split()))
