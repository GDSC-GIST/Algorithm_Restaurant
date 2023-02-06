import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for i in range(n): heapq.heappush(heap, int(sys.stdin.readline()))

answer = 0
while len(heap)>=2:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    answer += first + second
    if len(heap) == 0: break
    else: heapq.heappush(heap, first + second)

print(answer)