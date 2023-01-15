import sys
input=sys.stdin.readline
nums=[]
n=int(input())
for _ in range(n):
  nums.append(int(input()))

min_need=4
nums.sort()
for i,e in enumerate(nums):
  end=4 if i<n-4 else n-i-1
  for k in range(end,0,-1):
    if nums[i+k]<e+5:
      min_need=min(4-k,min_need)
      break
  if min_need==0:
    break
print(min_need)
