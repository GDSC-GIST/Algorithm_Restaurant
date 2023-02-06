import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

dp = [0]*n
dp[0] = sequence[0]

for i in range(1,n):
    for j in range(i):
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i], dp[j] + sequence[i])
        else:
            dp[i] = max(dp[i], sequence[i])

print(max(dp))
