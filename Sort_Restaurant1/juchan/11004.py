import sys

input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
print(nums[K-1])
# list sort 메소드는 O(nlogn)의 시간복잡도를 가진다.
# 백준기준 메모리 646904KB, 시간 2828ms

# from heapq import heappush, heappop

# heap = []

# for num in nums:
#     heappush(heap, num)

# ans = 0
# for i in range(K):
#     ans = heappop(heap)

# print(ans)
# heapq 모듈을 사용하면 O(nlogn)의 시간복잡도를 가진다.
# 백준기준 메모리 696680KB, 시간 4016ms

