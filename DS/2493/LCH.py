import sys

n = int(input())
towers = list(map(int, sys.stdin.readline().split()))
stack = [(0, 1000000000)]
ans = []
for i, t in enumerate(towers):
    while stack:
        if stack[-1][1] > t:
            break
        stack = stack[:-1]
    if not stack:
        ans.append("0")
    else:
        ans.append(str(stack[-1][0]))
    stack.append((i+1, t))
print(" ".join(ans))
