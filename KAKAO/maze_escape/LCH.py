from collections import deque


d = ['u', 'r', 'l', 'd']
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

    
def solution(n, m, x, y, r, c, k):
    if (x + y - r - c - k) % 2:
        return "impossible"
    
    s = deque()
    s.append([x, y, []])
    while s:
        curx, cury, route = s.pop()
        if len(route) == k and curx == r and cury == c:
            return "".join(route)
        # COOOOOOOOOOOL!
        if abs(r - curx) + abs(c - cury) > k - len(route):
            continue
        for i in range(4):
            if curx+dx[i] < 1 or curx+dx[i] > n or cury+dy[i] < 1 or cury+dy[i] > m:
                continue
            s.append([curx+dx[i], cury+dy[i], route+[d[i]]])
    
    return "impossible"
