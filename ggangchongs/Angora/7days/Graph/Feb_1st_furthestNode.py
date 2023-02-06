from collections import deque

def solution(n, edge):
    connect = [[] for _ in range(n+1)]
    for a,b in edge:
        connect[a].append(b)
        connect[b].append(a)
    
    visited = [0]*(n+1)
    visited[1] = 1
    queue = deque([1])
    while queue:
        now = queue.popleft()
        for next in connect[now]:
            if not visited[next]:
                visited[next] = visited[now] + 1
                queue.append(next)
    
    return visited.count(max(visited))

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))