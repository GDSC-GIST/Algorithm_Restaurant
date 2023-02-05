n, k = map(int, input().split())
ans = "<"
q = list(range(1, n+1))
count = 1
while q:
    front = q[0]
    q = q[1:]
    if count != k:
        q.append(front)
    else:
        ans += str(front) + ", "
        count = 0
    count += 1
ans = ans.rstrip(", ") + ">"
print(ans)
