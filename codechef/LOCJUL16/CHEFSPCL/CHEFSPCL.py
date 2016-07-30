def memo(f):
    mem = {}
    def ret(a, b, k, digit_count, mod_vals, overshot_a, undershot_b):
        key = (a, b, k, digit_count, mod_vals, overshot_a, undershot_b)
        if key not in mem: mem[key] = f(a, b, k, digit_count, mod_vals, overshot_a, undershot_b)
        return mem[key]
    return ret

@memo
def digit_dp(a, b, k, digit_count, mod_vals, overshot_a, undershot_b):
    '''
    Using digit DP
    keeping as states:
    - # of digit
    - x = num % K, we can happen by doing x * 10 + new_digit
    - bool, did we use a bigger digit for pos `i` than `a[i]`
    - bool, did we use a smaller digit for pos `i` than `b[i]`
    '''
    if digit_count == len(b): return 1
    start = 1 if overshot_a else a[digit_count]
    end = 9 if undershot_b else b[digit_count]
    count = 0
    for n in range(start, end + 1):
        if n > 0 and n % k == 0: continue
        mod_vals2 = tuple((x * 10 + n) % k for x in mod_vals)
        if 0 in mod_vals2: continue
        if (len(mod_vals2) > 0 or n != 0) and n % k not in mod_vals2: mod_vals2 += (n % k,)
        # Use the symmetries in 6 to reduce the computations
        if k == 6: mod_vals2 = tuple(x % 3 for x in mod_vals2)
        count += digit_dp(a, b, k, digit_count + 1, mod_vals2, overshot_a or n > a[digit_count], undershot_b or n < b[digit_count])
    return count

def solve(a, b, k):
    b = str(b)
    a = str(a)
    a = ('0' * (len(b) - len(a))) + a
    a = tuple(int(x) for x in a)
    b = tuple(int(x) for x in b)
    return digit_dp(a, b, k, 0, tuple(), False, False)
    
if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print solve(*map(int, raw_input().split()))
