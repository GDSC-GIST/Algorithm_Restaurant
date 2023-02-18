import sys
from collections import deque


r, c = map(int, input().split())
maze = [list(sys.stdin.readline()) for i in range(r)]

l = []
visitedj = [[0] * c for i in range(r)]
visitedf = [[0] * c for i in range(r)]
for row in range(r):
    for col in range(c):
        if maze[row][col] == 'J':
            l.append((row, col, 'J', 1))
            visitedj[row][col] = 1
        if maze[row][col] == 'F':
            l.append((row, col, 'F', 1))
            visitedf[row][col] = 1

l.sort(key=lambda x:x[2])
q = deque(l)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while q:
    x, y, z, t = q.popleft()
    if z == 'J':
        for i in range(4):
            if x+dx[i] < 0 or x+dx[i] >= r or y+dy[i] < 0 or y+dy[i] >= c:
                print(t)
                exit(0)
            if visitedj[x+dx[i]][y+dy[i]] or maze[x+dx[i]][y+dy[i]] in ('#', 'F'):
                continue
            visitedj[x+dx[i]][y+dy[i]] = 1
            q.append((x+dx[i], y+dy[i], z, t+1))
    else:
        for i in range(4):
            if x+dx[i] < 0 or x+dx[i] >= r or y+dy[i] < 0 or y+dy[i] >= c:
                continue
            if visitedf[x+dx[i]][y+dy[i]] or maze[x+dx[i]][y+dy[i]] == '#':
                continue
            visitedf[x+dx[i]][y+dy[i]] = 1
            maze[x+dx[i]][y+dy[i]] = 'F'
            q.append((x+dx[i], y+dy[i], z, t+1))
print("IMPOSSIBLE")
