NO = "No Food"

def solve(xs):
    res = []
    stack = []
    for x in xs:
        if x[0] == '1' and not stack: res.append(NO)
        elif x[0] == '1': res.append(stack.pop())
        else: stack.append(x[1])
    return '\n'.join(res)
        
if __name__ == '__main__':
    print solve([raw_input().split() for _ in range(int(raw_input()))])
