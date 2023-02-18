n, k = map(int, input().split())
selected = [int(input()) for i in range(n)]
visited = [0] * n

cur, count = 0, 0
while True:
    if visited[cur]:
        print(-1)
        break
    visited[cur] = 1
    count += 1
    if selected[cur] == k:
        print(count)
        break
    cur = selected[cur]
