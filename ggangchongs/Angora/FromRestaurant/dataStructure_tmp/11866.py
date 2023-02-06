import sys

n, k = map(int, sys.stdin.readline().split())

queue = []
for i in range(n):
    queue.append(i+1)

count = 1
answer = []
while len(queue) != 0:
    if count != k:
        tmp = queue.pop(0)
        queue.append(tmp)
        count += 1
    else:
        answer.append(queue.pop(0))
        count = 1

print("<", end='')
for i,a in enumerate(answer):
    if i == len(answer)-1: print(a, end='')
    else: print(a, end=', ')
print(">", end='')