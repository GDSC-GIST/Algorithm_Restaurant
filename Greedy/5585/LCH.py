n = 1000 - int(input())
arr = [500, 100, 50, 10, 5, 1]
ans = 0
for coin in arr:
    ans += n // coin
    n %= coin
print(ans)
