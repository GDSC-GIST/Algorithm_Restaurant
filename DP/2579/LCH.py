n = int(input())

stair = [int(input()) for i in range(n)]

dp = [[0] * 300, [0] * 300]
dp[0][0] = stair[0]
if n > 1:
    dp[0][1], dp[1][1] = stair[1], stair[0] + stair[1]

for i in range(2, n):
    dp[0][i] = stair[i] + max(dp[0][i-2], dp[1][i-2])
    dp[1][i] = stair[i] + max(dp[0][i-1], dp[0][i-2], dp[1][i-2])

print(max(dp[0][n-1], dp[1][n-1]))
