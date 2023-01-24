import sys

n, k = map(int,sys.stdin.readline().split())
dp = [k+1]*(k+1)
dp[0] = 0
coinList = []
for i in range(n):
    newCoin = int(sys.stdin.readline())
    if newCoin <= k:
        coinList.append(newCoin)
        dp[newCoin] = 1

for i in range(1, k+1):
    if dp[i] != 1:
        for coin in coinList:
            if i > coin:
                if dp[i-coin] != k+1:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[k] != k+1: print(dp[k])
else: print(-1)
