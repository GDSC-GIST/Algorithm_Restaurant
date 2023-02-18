t = int(input())
while t:
    n = int(input())
    board = [[0] * n for i in range(n)]

    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    q = [(sx, sy, 0)]
    board[sx][sy] = 1
    while q:
        x, y, count = q[0]
        del q[0]
        if x == ex and y == ey:
            print(count)
            break
        for i in range(8):
            if x + dx[i] < 0 or x + dx[i] >= n or y + dy[i] < 0 or y + dy[i] >= n:
                continue
            if board[x+dx[i]][y+dy[i]]:
                continue
            board[x+dx[i]][y+dy[i]] = 1
            q.append((x+dx[i], y+dy[i], count+1))
    t -= 1
