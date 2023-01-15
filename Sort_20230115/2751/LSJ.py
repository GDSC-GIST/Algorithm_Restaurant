import sys
input=sys.stdin.readline
nums=[]
for _ in range(int(input())):
  nums.append(int(input()))

for i in sorted(nums):
  print(i)
