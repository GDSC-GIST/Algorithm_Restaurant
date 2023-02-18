import sys
from collections import deque


"""
TLE with python3, but AC with pypy3
https://doc.pypy.org/en/latest/
"""


n, m, k = map(int, input().split())
maze = [list(map(int, list(input()))) for i in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[[9999999] * m for i in range(n)] for j in range(k+1)]
q = deque([(0, 0, 1, k)])
visited[k][0][0] = 1
while q:
    x, y, d, b = q.popleft()
    if x == n-1 and y == m-1:
        print(d)
        exit(0)
    
    d += 1
    for i in range(4):
        if x + dx[i] < 0 or x + dx[i] >= n or y + dy[i] < 0 or y + dy[i] >= m:
            continue
        if maze[x+dx[i]][y+dy[i]] == 1 and b == 0:
            continue
        if maze[x+dx[i]][y+dy[i]] == 0 and visited[b][x+dx[i]][y+dy[i]] <= d or \
            maze[x+dx[i]][y+dy[i]] == 1 and visited[b-1][x+dx[i]][y+dy[i]] <= d:
            continue
        if maze[x+dx[i]][y+dy[i]]:
            visited[b-1][x+dx[i]][y+dy[i]] = d
            q.append((x+dx[i], y+dy[i], d, b-1))
        else:
            visited[b][x+dx[i]][y+dy[i]] = d
            q.append((x+dx[i], y+dy[i], d, b))
print(-1)
