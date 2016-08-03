def solve(xss):
    cities = set()
    for x, y in xss:
        cities.add(x)
        cities.add(y)
    return len(cities)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print solve([map(int, raw_input().split()) for _ in range(int(raw_input()))])
