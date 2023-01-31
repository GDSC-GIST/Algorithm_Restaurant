n, k = map(int, input().split())
coins = [int(input())  for i in range(n)]
for coin in coins:
    if coin > k:
        coins.remove(coin)
        
dp = [99999] * 100001
for coin in coins:
    dp[coin] = 1
for i in range(10000):
    for coin in coins:
        dp[i+coin] = min(dp[i+coin], dp[i]+1)
if dp[k] == 99999:
    dp[k] -= 100000
print(dp[k])
