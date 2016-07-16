# def intuition(n):
#     import itertools
#     import collections
#     xss = itertools.product([0, 1], repeat=n)

#     combi = set()
#     combis = collections.defaultdict(list)
#     all_odd = set()
#     all_even = set()
#     for xs in xss:
#         mod = [0, 0]
#         for i in range(len(xs)):
#             for j in range(i + 1, len(xs) + 1):
#                 s = sum(xs[i:j])
#                 mod[s % 2] += 1
#         # print ''.join(map(str, xs)), mod
#         all_odd.add(mod[1])
#         all_even.add(mod[0])
#         combi.add(tuple(mod))
#         combis[tuple(mod)].append(''.join(map(str, xs)))

#     # print 'odd = {}, even = {}'.format(len(all_odd), len(all_even))
#     print '{} combi = {}'.format(n, combi)
#     # for x, y in combis.items():
#     #     print x, y
    
# # for i in range(11):
# #     intuition(i)
# #     solve(i)

# # intuition(i)

# for i in range(11):
#     intuition(i)
#     solve(i, 0, 0)


def geom(n):
    '''0 1 3 6 10 15 21 ...'''
    return n * (n + 1) / 2

def pos(n):
    return (n + 1) / 2

def solve(n, e, o):
    geo = geom(n)
    for i in range(pos(n) + 1):
        y = i * (n + 1 - i)
        x = geo - y
        pair = (x, y)
        if pair == (e, o):
            ret = [0] * n
            if i > 0: ret[i - 1] = 1
            return ' '.join(map(str, ret))
    return -1
    
if __name__ == "__main__":
    for t in range(int(raw_input())):
        N = int(raw_input())
        E, O = map(int, raw_input().split())
        res = solve(N, E, O)
        print "{}".format(res)
