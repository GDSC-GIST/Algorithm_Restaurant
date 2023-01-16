import sys

input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)

nums.sort()
for i in range(n):
    print(nums[i])

# list sort 메소드는 O(nlogn)의 시간복잡도를 가진다.
# 백준기준 메모리 114327KB, 시간 124ms

# from heapq import heappush, heappop

# heap = []

# for _ in range(n):
#    num = int(input())
#    heappush(heap, num)

# for i in range(n):
#    print(heappop(heap))
    
# heapq 모듈을 사용하면 O(nlogn)의 시간복잡도를 가진다.
# 백준기준 메모리 115268KB, 시간 140ms