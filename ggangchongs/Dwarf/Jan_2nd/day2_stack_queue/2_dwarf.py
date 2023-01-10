def solution(arr):
    answer = []
    temp = -1
    for candidate in arr:
        if temp != candidate:
            answer.append(candidate)
        temp = candidate
    return answer
    