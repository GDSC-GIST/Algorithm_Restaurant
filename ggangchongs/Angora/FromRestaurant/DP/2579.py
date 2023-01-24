import sys

n = int(sys.stdin.readline())
stair = []
for i in range(n):
    stair.append(int(sys.stdin.readline()))

memo = []
memo.append([0,0])
memo.append([stair[0],stair[0]])
for i in range(2,n+1):
    memo.append([
        max(memo[i-2]) + stair[i-1],
        memo[i-1][0] + stair[i-1]
    ])

print(max(memo[n]))