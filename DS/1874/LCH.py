import sys

def sol():
    n = int(sys.stdin.readline())
    stack = []
    goal = [int(sys.stdin.readline()) for i in range(n)]
    ans = []
    num = 1
    for x in goal: 
        while x >= num:
            stack.append(num)
            num += 1
            ans += '+'
        if stack[-1] != x:
            print("NO")
            return -1
        stack = stack[:-1]
        ans += '-'
    print("\n".join(ans))

sol()
