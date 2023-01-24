import sys

n = int(sys.stdin.readline())
answer = 0

if n <= 5:
    if n == 3 or n == 5: answer = 1
    else: answer = -1
elif n > 5:
    memo = [0]*(n+1)
    memo[0], memo[1], memo[2] = 0,0,0
    memo[3], memo[4], memo[5] = 1,0,1
    for i in range(6, n+1):
        if memo[i-3] == 0 and memo[i-5] == 0: continue
        elif memo[i-3] == 0: memo[i] = memo[i-5]+1
        elif memo[i-5] == 0: memo[i] = memo[i-3]+1
        else: memo[i] = min(memo[i-3]+1,
                            memo[i-5]+1)
    answer = memo[n]

if answer == 0: print(-1)
else: print(answer)


'''
3 -> 1
4 -> -1
5 -> 1
6 -> 2
7 -> -1
8 -> 2
9 -> 

'''