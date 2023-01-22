import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort(key=lambda x: (x[1],x[0]))

ans = 0
end = 0
for conf in arr:
    if conf[0] >= end:
        ans += 1
        end = conf[1]
print(ans)
