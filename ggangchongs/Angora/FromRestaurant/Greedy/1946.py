import sys

t = int(sys.stdin.readline())
for tt in range(t):
    
    n = int(sys.stdin.readline())
    tmp = []
    answer = n
    for nn in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
    tmp.sort()
    tmpMax = tmp[0][1]
    for i in range(1, n):
        if tmpMax < tmp[i][1]: answer -= 1
        else: tmpMax = tmp[i][1]
    print(answer)
        
        
'''
3 2
1 4
4 1
2 3
5 5
---
5 5
4 1
3 2
2 3
1 4
'''