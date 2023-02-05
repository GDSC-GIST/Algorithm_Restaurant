import sys

from queue import PriorityQueue

q = PriorityQueue()
n = int(input())
for i in range(n):
    q.put(int(sys.stdin.readline()))

ans = 0
for i in range(n-1):
    a, b = q.get(), q.get()
    ans += a + b
    q.put(a+b)

print(ans)
