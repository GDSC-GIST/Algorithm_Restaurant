n = int(input())
g = {}
for i in range(1, n+1):
    g[i] = []
    
for i in range(int(input())):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

visited = [0] * (n+1)
q = [1]
while q:
    cur = q.pop()
    if visited[cur]:
        continue
    visited[cur] = 1
    for v in g[cur]:
        q.append(v)

print(sum(visited)-1)
