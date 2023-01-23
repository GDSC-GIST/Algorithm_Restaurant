import sys

n = int(sys.stdin.readline())

def fibo_dp(n):
    fiboTable = [0]*(n+1)
    fiboTable[0], fiboTable[1] = 0, 1
    for i in range(2, n+1):
        fiboTable[i] = fiboTable[i-1] + fiboTable[i-2]
    return fiboTable[n]

print(fibo_dp(n))