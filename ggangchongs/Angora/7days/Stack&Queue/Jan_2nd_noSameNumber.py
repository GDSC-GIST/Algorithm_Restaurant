from collections import deque

def solution(arr):
    answer = []
    queue = deque(arr)
    
    tmp = -1
    while len(queue) != 0:
        test = queue.popleft()
        if tmp != test:
            answer.append(test)
            tmp = test
    return answer

def solution_best(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        # a[-1:] = [마지막 값]
        a.append(i)
    return a
# 리스트로 하면 효율성에서 에러나서 그냥 큐 사용했는데
# 코드의 효율성 문제였던건가? 아님 문제 개편이후 변경된건가