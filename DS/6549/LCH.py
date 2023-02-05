import sys

while True:
    arr = list(map(int, sys.stdin.readline().split()))
    n = arr.pop(0)
    
    if n == 0:
        break
    
    stack = []
    ans = 0
    
    for i in range(n):
        while len(stack) != 0 and arr[stack[-1]] > arr[i]:
            temp = stack.pop()
            
            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            ans = max(ans, width * arr[temp])
        stack.append(i)
        
    while len(stack) != 0:
        temp = stack.pop()
        
        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1
        ans = max(ans, width * arr[temp])
    
    print(ans)
