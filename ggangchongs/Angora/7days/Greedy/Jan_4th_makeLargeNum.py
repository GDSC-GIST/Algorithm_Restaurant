def solution(number, k):
    
    numList = list(number)
    delete = 0
    answer = ''
    
    for num in numList:
        while len(answer) != 0 and delete < k and answer[-1] < num:
            answer = answer[:-1]
            delete += 1
        answer += num
    
    if delete != k: # for 4321
        return answer[:-1*(k-delete)]
    return answer

number = "4321"
k = 2
print(solution(number, k))
print(number[:-1])
'''
1924 2
1231234 3
4177252841 4
312924 2
'''