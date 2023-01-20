import sys

fibo = [0,1]
def createFibonacci(limit):
    i = len(fibo)-2
    while fibo[-1] < limit:
        fibo.append(fibo[i]+fibo[i+1])
        i += 1

t = int(sys.stdin.readline())
nums = []
maxN = 0
f = []
for _ in range(t):
    tmp = int(sys.stdin.readline())
    maxN = max(maxN, tmp)
    nums.append(tmp)
    f.append([])

createFibonacci(maxN)

for i in range(len(fibo)-1, -1, -1):
    for j, n in enumerate(nums):
        if 0 < n and fibo[i] <= n:
            f[j].append(fibo[i])
            nums[j] -= fibo[i]

for fList in f:
    for i in range(len(fList)-1, -1, -1):
        print(fList[i], end=' ')
    print()