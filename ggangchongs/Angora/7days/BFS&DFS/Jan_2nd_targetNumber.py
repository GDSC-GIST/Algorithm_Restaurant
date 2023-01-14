# 모르겠어서 답지 봤음 ㅠ
def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    while queue:
        val, index = queue.pop()
        index += 1
        if index < n:
            queue.append([val + numbers[index], index])
            queue.append([val - numbers[index], index])
        else:
            if val == target: answer += 1
    return answer