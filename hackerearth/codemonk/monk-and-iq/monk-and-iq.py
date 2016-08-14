import heapq

def solve(c, iqs, piqs):
    res = []
    q = [(0, i, 0, (0, 0)) for i in range(len(iqs) + 1, c + 1)]
    q += [(iq, i, 1, (0, iq)) for i, iq in enumerate(iqs, 1)]
    heapq.heapify(q)
    for iq in piqs:
        _, course, student_count, last_iqs = q[0]
        res.append(course)
        student_count += 1
        last_iqs = (last_iqs[1], iq)
        heapq.heapreplace(q, (sum(last_iqs) * student_count, course, student_count, last_iqs))
    return ' '.join(str(r) for r in res)

if __name__ == '__main__':
    ''' Once again one of the input is broken on codemonk ... '''
    c, p, _ = map(int, raw_input().split())
    iqs = map(int, raw_input().split())
    piqs = map(int, raw_input().split())
    piqs += [0] * (p - len(piqs)) # because input is truncated ...
    print solve(c, iqs, piqs)
