import collections

def solve(nss, mss, g, h):
    skills = collections.Counter(skill for skill, _ in nss)
    skills_n_mastery = collections.Counter(tuple(x) for x in nss)
    for skill, mastery in mss:
        if g and skills[skill]:
            g -= 1
            skills[skill] -= 1
        if h and skills_n_mastery[(skill, mastery)]:
            h -= 1
            skills_n_mastery[(skill, mastery)] -= 1
        if not g and not h: return "Great"
    if not g: return "Good"
    return ":("

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        m, n = map(int, raw_input().split())
        mss = [map(int, raw_input().split()) for _ in range(m)]
        nss = [map(int, raw_input().split()) for _ in range(n)]
        g, h = map(int, raw_input().split())
        print solve(nss, mss, g, h)
