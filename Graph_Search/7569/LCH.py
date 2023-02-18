import sys
from collections import deque


m, n, h = map(int, input().split())
tmt = []

# 사람들이 괜히 리스트 말고 deque를 쓰는게 아니었다.. 짱빠르네
q = deque()
for i in range(h):
    tmt_floor = []
    for j in range(n):
        tmt_line = list(map(int, sys.stdin.readline().split()))
        for k in range(m):
            if tmt_line[k] == 1:
                q.append((i, j, k, 1))
        tmt_floor.append(tmt_line)
    tmt.append(tmt_floor)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
while q:
    x, y, z, d = q.popleft()
    for i in range(6):
        if x + dx[i] < 0 or x + dx[i] >= h or \
            y + dy[i] < 0 or y + dy[i] >= n or \
            z + dz[i] < 0 or z + dz[i] >= m:
            continue
        if not tmt[x+dx[i]][y+dy[i]][z+dz[i]]:
            tmt[x+dx[i]][y+dy[i]][z+dz[i]] = d+1
            q.append((x+dx[i], y+dy[i], z+dz[i], d+1))

ans = 0
for i in tmt:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            if k > ans:
                ans = k

print(ans - 1)
