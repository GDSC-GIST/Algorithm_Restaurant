n, k = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
dp = [[0]*(k+1) for i in range(n+1)]
for i in range(n):
    for w in range(k+1):
        if a[i-1][0] <= w:
            dp[i][w] = max(a[i-1][1]+dp[i-1][w-a[i-1][0]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]
print(dp[n-1][k])
