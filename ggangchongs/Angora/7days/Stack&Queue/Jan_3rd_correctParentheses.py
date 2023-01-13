def solution(s):
    answer = True
    sList = list(s)
    stack = []
    
    for i in sList:
        if i == '(': stack.append(i)
        elif i == ")":
            if stack[-1:] == ["("]:
                stack.pop()
            else:
                answer = False
                break
    if len(stack) != 0: answer = False
    return answer