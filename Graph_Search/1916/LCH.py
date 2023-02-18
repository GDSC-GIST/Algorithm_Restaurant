import sys


n = int(input())
m = int(input())
g = [[] for i in range(n+1)]

for i in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    g[s].append((e, c))


# sort graph by cost to reduce calculation
for i in g:
    i.sort(key=lambda x: x[1])


start, end = map(int, input().split())
visited = [999999999] * (n+1) # maximum : NM
q = [(start, 0)]
while q:
    cur, cost = q[0]
    del q[0]
    for city, fee in g[cur]:
        if cost + fee < visited[city]:
            visited[city] = cost + fee
            q.append((city, cost + fee))

print(visited[end])
