n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()

ans = 4
for i in range(n):
    temp = 1
    for j in range(i + 1, i + 5):
        if j == n:
            break
        if a[j] - a[i] < 5:
            temp += 1
    ans = min(ans, 5 - temp)

print(ans)
