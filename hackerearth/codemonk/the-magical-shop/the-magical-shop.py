def solve(n, mod, xs):
    stock = n
    bought = 0
    for x in xs:
        if x == '1': bought = (bought + stock) % mod
        stock = stock**2 % mod
    return bought
            
if __name__ == '__main__':
    n, mod = map(int, raw_input().split())
    print solve(n, mod, raw_input())
