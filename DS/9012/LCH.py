n = int(input())
for i in range(n):
    s = input()
    ans = "YES"
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack = stack[:-1]
            else:
                ans = "NO"
                break
    if stack:
        ans = "NO"
    print(ans)
