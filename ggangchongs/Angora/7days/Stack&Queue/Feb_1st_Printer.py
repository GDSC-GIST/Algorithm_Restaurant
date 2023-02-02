def solution(priorities, location):
    answer = 0
    
    while len(priorities) != 0:
        tmp = priorities.pop(0)
        
        if len(priorities) == 0:
            return answer + 1
        
        if tmp < max(priorities): # 출력 불가
            priorities.append(tmp)
            if location == 0: location = len(priorities)-1
            else: location -= 1
        else: # 출력 가능
            answer += 1
            if location == 0: return answer
            else: location -= 1

priorities = [1, 1, 2, 3, 2, 1]
location = 	0
print(solution(priorities, location))


tmp = []