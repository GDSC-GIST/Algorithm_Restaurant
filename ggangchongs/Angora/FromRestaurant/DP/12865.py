# 0/1 knapsack
def knapsack(num, maxWeight, weightList, valueList):
    dp = [[0 for _ in range(maxWeight+1)] for _ in range(num+1)]
    
    for i in range(1, num + 1):
        for j in range(1, maxWeight + 1):
            if weightList[i-1] > j: # 지금 물건을 넣을 수 없다면
                dp[i][j] = dp[i-1][j] # 이전 칸을 그대로
            else: # 지금 물건을 넣을 수 있다면
                dp[i][j] = max(dp[i-1][j],
                               # 이전 칸을 그대로 or
                               dp[i-1][j - weightList[i-1]] + valueList[i-1]
                               # 이전 물건을 더하기 전
                               # + 지금 물건의 value
                               )
    return dp[num][maxWeight]


# driver code
import sys

n, k = map(int, sys.stdin.readline().split())
wList = [0]*n
vList = [0]*n
for i in range(n):
    wList[i],  vList[i] = map(int, sys.stdin.readline().split())
print(knapsack(n, k, wList, vList))