n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr = arr[::-1]
ans = 0
for coin in arr:
    ans += k // coin
    k %= coin
print(ans)
