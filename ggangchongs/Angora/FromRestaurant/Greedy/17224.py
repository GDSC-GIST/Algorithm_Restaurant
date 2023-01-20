import sys

n, l, k = map(int, sys.stdin.readline().split())
correctHard = 0
correctEasy = 0
for i in range(n):
    easy, hard = map(int, sys.stdin.readline().split())
    if hard <= l: correctHard += 1
    elif easy <= l: correctEasy += 1

if correctHard >= k: print(k*140)
else:
    k -= correctHard
    if correctEasy >= k:
        print(correctHard*140 + k*100)
    else: print(correctHard*140 + correctEasy*100)