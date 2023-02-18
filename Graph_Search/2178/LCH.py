n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for i in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * m for i in range(n)]
q = [(0, 0, 1)]
visited[0][0] = 1
while q:
    x, y, count = q[0]
    del q[0]
    if x == n-1 and y == m-1:
        print(count)
        break
    for i in range(4):
        if x + dx[i] < 0 or x + dx[i] >= n or y + dy[i] < 0 or y + dy[i] >= m:
            continue
        if maze[x+dx[i]][y+dy[i]] == 0 or visited[x+dx[i]][y+dy[i]]:
            continue
        visited[x+dx[i]][y+dy[i]] = 1
        q.append((x+dx[i], y+dy[i], count+1))
