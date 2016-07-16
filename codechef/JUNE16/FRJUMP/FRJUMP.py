MOD = 1000000007
EPSILON = 0.9999999999999

def brute_prod(xs):
    prod = 1
    for x in xs:
        prod *= x
    return prod % MOD

def mod_prod(xs):
    prod = 1
    for x in xs:
        prod = (prod * x) % MOD
    return prod

def brute_first_digit(xs):
    prod = 1
    for x in xs:
        prod *= x
    return str(prod)[0]

import math
def log_first_digit(xs):
    prod = 0
    for x in xs:
        prod += math.log10(x)
    return str(10**(prod - int(prod)))[0]

def get_first_digit(logs):
    val = 10**(logs - int(logs))
    x = val - int(val)
    res = '0'
    if x >= EPSILON:
        res = str(int(val) + 1)
    else:
        res = str(int(val))
    return res

def smart_prod(xs, xs_logs, r):
    prod = 1
    logs = 0
    for i in range(0, len(xs), r):
        prod = (prod * xs[i]) % MOD
        logs += xs_logs[i]
    first_digit = get_first_digit(logs)
    return (prod, logs, first_digit)

def memoish(xs):
    memo = {}
    xs_logs = [math.log10(x) for x in xs]
    return xs_logs, memo

def update_memo(prod, logs, delta_prod, delta_log):
    new_prod = (prod * delta_prod) % MOD
    new_logs = logs + delta_log
    first_digit = get_first_digit(new_logs)
    return (new_prod, new_logs, first_digit)

def update_memoish(xs, xs_logs, memo, sq_n, index, val, asked):
    idx = index - 1
    val_log = math.log10(val)
    delta_prod = (pow(xs[idx], MOD - 2, MOD) * val) % MOD
    delta_log = - xs_logs[idx] + val_log
    for i in range(1, sq_n + 1):
        if idx % i == 0 and i in memo and asked.get(i, 0) > 0:
            prod, logs, _ = memo[i]
            memo[i] = update_memo(prod, logs, delta_prod, delta_log)

    xs[idx] = val
    xs_logs[idx] = val_log
    return xs, xs_logs, memo


def ask_counter(qs):
    asked = {}
    for q in qs:
        if q[0] == 1: continue
        idx = q[1]
        asked[idx] = asked.get(idx, 0) + 1
    return asked

def remove_useless_q(qs):
    # remove trailing update
    rqs = qs[::-1]
    for i in range(len(rqs)):
        if rqs[i][0] == 2: break
    rqs = rqs[i:]
    # remove double updates
    res = []
    seen = set()
    for q in rqs:
        if q[0] == 2:
            seen = set()
            res.append(q)
        elif q[1] not in seen:
            seen.add(q[1])
            res.append(q)
    return res[::-1]

    
def solve(xs, instructions):
    instructions = remove_useless_q(instructions)
    asked = ask_counter(instructions)
    sq_n = int(math.sqrt(len(xs)))
    xs_logs, memo = memoish(xs)
    res = []
    for instruction in instructions:
        if instruction[0] == 1:
            xs, xs_logs, memo = update_memoish(xs, xs_logs, memo, sq_n, instruction[1], instruction[2], asked)
        elif instruction[1] in memo:
            prod, logs, first_digit = memo[instruction[1]]
            asked[instruction[1]] -= 1
            res.append((first_digit, prod))
        else:
            prod, logs, first_digit = smart_prod(xs, xs_logs, instruction[1])
            if instruction[1] < sq_n + 1 and asked.get(instruction[1], 0) > 0: memo[instruction[1]] = (prod, logs, first_digit)
            res.append((first_digit, prod))
    return '\n'.join('{} {}'.format(*x) for x in res)
    
if __name__ == '__main__':
    _ = raw_input()
    xs = map(int, raw_input().split())
    queries = []
    for _ in range(int(raw_input())):
        queries.append(map(int, raw_input().split()))
    res = solve(xs, queries)
    print '{}'.format(res)
