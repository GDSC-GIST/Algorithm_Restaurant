import sys

n = int(sys.stdin.readline())
topList = list(map(int, sys.stdin.readline().split()))

indexStack, answer = [1],[0]
for i, top in enumerate(topList):
    if i == 0: continue
    else:

        while topList[indexStack[-1]-1] < top:
            indexStack.pop()
            if len(indexStack) == 0: break
        if len(indexStack) == 0: answer.append(0)
        else: answer.append(indexStack[-1])
        indexStack.append(i+1)

for i in answer: print(i, end=' ')