import math

def solution(progresses, speeds):
    answer = []
    stack = []
    tmpCount = 0
    
    for i in range(len(speeds)):
        tmp = math.ceil((100-progresses[i])/speeds[i])
        
        if stack[-1:] < [tmp]:
            # print([] < [3]) # true
            # -> stack이 비어있을 경우를 고려할 필요 없음
            answer.append(tmpCount)
            # 처음에 바로 0을 삽입하기 때문에,
            # return 시기에서 제외함
            stack.append(tmp)
            tmpCount = 1
        else:
            # 대기하게 될 작업들일 경우
            # 한번에 배포할 개수를 up
            tmpCount += 1
    
    answer.append(tmpCount) # 마지막 배포 개수를 append

    return answer[1:] # 맨 처음의 0 제외





'''
93 -> 1*7 -> 7일
30 -> 30*3 -> 3일 -> 7일
55 -> 5*9 -> 9일

[95, 90, 99, 99, 80, 99]
[1, 1, 1, 1, 1, 1]
'''

progresses = [93, 30, 55]
speeds = 	[1, 30, 5]
print(solution(progresses, speeds))