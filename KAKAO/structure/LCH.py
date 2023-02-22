def solution(board, skill):
    n = len(board)
    m = len(board[0])
    acc = [[0] * m for i in range(n)]
    for s in skill:
        t, r1, c1, r2, c2, deg = s
        deg *= (t - 1) * 2 - 1
        
        acc[r1][c1] += deg
        if r2 + 1 < n:
            acc[r2+1][c1] += -deg
        if c2 + 1 < m:
            acc[r1][c2+1] += -deg
        if r2 + 1 < n and c2 + 1 < m:
            acc[r2+1][c2+1] += deg
    
    for i in range(1, n):
        for j in range(m):
            acc[i][j] += acc[i-1][j]
    
    for i in range(n):
        for j in range(1, m):
            acc[i][j] += acc[i][j-1]
    
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + acc[i][j] > 0:
                answer += 1
    
    return answer
