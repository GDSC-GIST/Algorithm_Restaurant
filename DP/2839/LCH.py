n = int(input())

dp = [9999] * 5001
dp[3], dp[5] = 1, 1
for i in range(6, n+1):
    dp[i] = min(dp[i], dp[i-3] + 1, dp[i-5] + 1)

if dp[n] == 9999:
    dp[n] -= 10000

print(dp[n])
