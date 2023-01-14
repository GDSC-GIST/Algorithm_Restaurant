import sys

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()

# 현재의 수를 1이라 할때,
# 1 ~ 5 사이에 몇개의 숫자가 있는지 확인 -> 그 개수가 가장 작은 것으로 세팅
count = 0
for i in range(len(nums)-1):
    first = nums[i]
    j = i+1
    tmp = 1
    while j < len(nums):
        if nums[j] < first+5:
            tmp += 1
            j += 1
        else: break
    count = max(count, tmp)

if len(nums) == 1: count = 1

if count >= 5: print(0)
else: print(5-count)