import sys

n, k = map(int, sys.stdin.readline().split())
bill = []
for i in range(n):
    bill.append(int(sys.stdin.readline()))

answer = 0
for i in range(len(bill)-1, -1, -1):
    if k < 0: break
    answer += k//bill[i]
    k = k%bill[i]

print(answer)