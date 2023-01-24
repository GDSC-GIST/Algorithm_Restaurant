import sys

n = int(sys.stdin.readline())
game = []
# 한 줄 짜리로 해도 메모리는 비슷함
maxMap = [[0,0,0],[0,0,0]]
minMap = [[0,0,0],[0,0,0]]

j = 1
for i in range(n):
    j = 1-j
    a, b, c = map(int, sys.stdin.readline().split())
    if i == 0:
        maxMap[j][0], maxMap[j][1], maxMap[j][2] = a, b, c
        minMap[j][0], minMap[j][1], minMap[j][2] = a, b, c
    else:
        maxMap[j][0] = max(maxMap[1-j][0], maxMap[1-j][1]) + a
        maxMap[j][1] = max(maxMap[1-j]) + b
        maxMap[j][2] = max(maxMap[1-j][1], maxMap[1-j][2]) + c
        
        minMap[j][0] = min(minMap[1-j][0], minMap[1-j][1]) + a
        minMap[j][1] = min(minMap[1-j]) + b
        minMap[j][2] = min(minMap[1-j][1], minMap[1-j][2]) + c

print(str(max(maxMap[j])) + " " + str(min(minMap[j])))
