import sys

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
for i in nums:
    print(i, end=' ')