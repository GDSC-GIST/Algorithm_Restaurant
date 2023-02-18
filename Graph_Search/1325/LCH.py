import sys
from collections import deque


"""
TLE with python3, but AC with pypy3
https://doc.pypy.org/en/latest/
"""


n, m = map(int, sys.stdin.readline().split())
g = [[] for i in range(n+1)]
for i in range(m):
    e, s = map(int, sys.stdin.readline().split())
    g[s].append(e)

ans = []
for i in range(1, n+1):
    visited = [0 for i in range(n+1)]
    q = deque()
    q.append(i)
    visited[i] = 1
    count = 1
    while q:
        cur = q.popleft()
        for j in g[cur]:
            if not visited[j]: # only add when not visited
                q.append(j)
                visited[j] = 1
                count += 1
    ans.append(count)

max_val = max(ans)
for i in range(n):
    if ans[i] == max_val:
        print(i+1, end=" ")
