n, l, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1])
ans = 0
for prob in arr:
    if k == 0:
        break
    if prob[1] <= l:
        ans += 140
        k -= 1
    elif prob[0] <= l:
        ans += 100
        k -= 1
print(ans)
