import collections

def solve(xs):
    foods = collections.defaultdict(lambda: 0)
    count = 0
    for food, pokemon in xs:
        foods[food] += 1
        if foods[pokemon] > 0: foods[pokemon] -= 1
        else: count += 1
    return count

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print solve([map(int, raw_input().split()) for _ in range(int(raw_input()))])
