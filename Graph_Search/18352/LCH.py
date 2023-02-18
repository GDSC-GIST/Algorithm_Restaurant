import sys


n, m, k, x = map(int, input().split())
g = {}
for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    if s not in g:
        g[s] = []
    g[s].append(e)

visited = [0] * (n+1)
q = [(x, 0)]
while q:
    cur, dist = q[0]
    del q[0] # fastest way to delete
    if visited[cur] or dist > k:
        continue
    dist += 1
    visited[cur] = dist
    if cur not in g:
        continue
    for i in g[cur]:
        q.append((i, dist))

ans = []
for i in range(n+1):
    if visited[i] == k+1:
        ans.append(i)
if not ans:
    ans.append(-1)
for i in ans:
    print(i)
