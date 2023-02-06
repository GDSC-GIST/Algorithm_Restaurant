import sys

t = int(sys.stdin.readline())

testStack = []
answer = "YES"
for i in range(t):
    tmpPS = list(sys.stdin.readline())
    
    for p in tmpPS:
        if p == '(': testStack.append(p)
        if p == ')':
            if testStack[-1:] == ['(']: testStack.pop()
            else: answer = "NO"; break
    if len(testStack) != 0: answer = "NO"
    print(answer)
    testStack.clear(); answer ="YES"
