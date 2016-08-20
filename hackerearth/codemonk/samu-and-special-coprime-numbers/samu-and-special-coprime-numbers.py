def gcd(a, b):
    if not b: return a
    return gcd(b, a % b)

def memo(f):
    mem = {}
    def ret(r, step_left, undershot, sum_digits, sum_square_digits):
        if not undershot: return f(r, step_left, undershot, sum_digits, sum_square_digits)
        key = (step_left, sum_digits, sum_square_digits)
        if key not in mem:
            mem[key] = f(r, step_left, undershot, sum_digits, sum_square_digits)
        return mem[key]
    return ret

@memo
def rec(r, step_left, undershot, sum_digits, sum_square_digits):
    if step_left == 0: return 1 if gcd(sum_square_digits, sum_digits) == 1 else 0
    d = (r / (10 ** (step_left - 1)) % 10)
    end = 9 if undershot else d
    count = 0
    for n in range(end + 1):
        count += rec(r, step_left - 1, undershot or n < d, sum_digits + n, sum_square_digits + n**2)
    return count
    
def solve(l, r):
    return rec(r, len(str(r)), False, 0, 0) - rec(l - 1, len(str(l - 1)), False, 0, 0)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print solve(*map(int, raw_input().split()))
