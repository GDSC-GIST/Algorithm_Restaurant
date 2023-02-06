import sys

n = int(sys.stdin.readline())

fruits = {}
for i in range(n):
    tmp, num = sys.stdin.readline().split()
    if tmp in fruits:
        fruits[tmp] += int(num)
    else:
        fruits[tmp] = int(num)

if 5 in fruits.values(): print("YES")
else: print("NO")
    