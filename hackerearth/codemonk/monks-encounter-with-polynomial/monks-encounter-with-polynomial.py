def eval(a, b, c, x):
    return ((a * x) + b) * x + c

def solve(a, b, c, k):
    start = 0
    end = k
    found = 0
    while start <= end:
        mid = (start + end) / 2
        val = eval(a, b, c, mid) 
        if val < k: start = mid + 1
        else:
            found = mid
            end = mid - 1
    return found
        
if __name__ == '__main__':
    for _ in range(int(raw_input())):
        a, b, c, k = map(int, raw_input().split())
        print solve(a, b, c, k)
