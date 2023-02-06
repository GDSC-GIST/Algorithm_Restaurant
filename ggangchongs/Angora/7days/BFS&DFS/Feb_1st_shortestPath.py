from collections import deque

def solution(maps):
    queue = deque()
    step = [(-1,0), (1,0), (0,-1), (0,1)] # 상 하 좌 우
    answer = bfs_maze(0,0, queue, step, maps)
    if answer == 1: return -1
    else: return answer

def bfs_maze(x,y, queue, step, maps):
    n,m = len(maps), len(maps[0])
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        for act in step:
            nx, ny = x + act[0], y + act[1]
            
            # 벗어나면 패스
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            # 벽이면 패스
            if maps[nx][ny] == 0: continue
            # 이동 가능할 경우
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))
    
    return maps[n-1][m-1]

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))