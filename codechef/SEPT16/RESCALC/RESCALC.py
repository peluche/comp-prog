import collections

def score_cookies(cs):
    score = len(cs)
    count = [0] * 6
    for c in cs: count[c - 1] += 1
    count.sort()
    used = 0
    for bonus, c in zip([4, 2, 1], count):
        c -= used
        used += c
        score += c * bonus
    return score

def solve(xss):
    scores = collections.defaultdict(lambda: [])
    for i, xs in enumerate(xss, 1):
        scores[score_cookies(xs)].append(i)
    winners = scores[max(scores)]
    if len(winners) > 1: return 'tie'
    if winners[0] == 1: return 'chef'
    return str(winners[0])

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        xss = [map(int, raw_input().split())[1:] for _ in range(int(raw_input()))]
        print solve(xss)
