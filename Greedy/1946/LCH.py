import sys

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    arr.sort()
    
    minimum = arr[0][1]
    ans = 1
    for i in range(1, n):
        if arr[i][1] < minimum:
            ans += 1
            minimum = arr[i][1]
    print(ans)
    