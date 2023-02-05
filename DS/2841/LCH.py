import sys

n, p = map(int, input().split())
melody = [sys.stdin.readline() for i in range(n)]

prets = [[] for i in range(7)]
ans = 0
for m in melody:
    l, p = map(int, m.split())
    while prets[l]:
        if p >= prets[l][-1]:
            break
        prets[l] = prets[l][:-1]
        ans += 1
    if prets[l]:
        if p == prets[l][-1]:
            continue
    prets[l].append(p)
    ans += 1

print(ans)
