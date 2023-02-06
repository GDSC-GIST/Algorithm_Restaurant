'''
1 2 3 4 -> 4
1 2 3 -> 4
1 2 -> 4 3
1 2 5 6 -> 4 3
1 2 5 -> 4 3 6
1 2 5 7 8 -> 4 3 6
 -> 4 3 6 8 7 5 2 1
'''

import sys

n = int(sys.stdin.readline())

candi = 1
stack, answer = [], []
correct = True
for i in range(n):
    target = int(sys.stdin.readline())
    while candi <= target:
        stack.append(candi)
        answer.append("+")
        candi += 1
    if stack[-1] == target:
        stack.pop()
        answer.append("-")
    else: correct = False; break

if correct == False: print("NO")
else:
    for a in answer: print(a)
