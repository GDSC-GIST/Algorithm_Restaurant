def solution(citations):
    citations.sort()
    count = []
    tmpCount = 0
    isAllZero = True
    for i in range(len(citations)):
        # [0,0,0,0,0] 예외 처리를 위함
        if citations[i] != 0: isAllZero = False
        
        if i == 0 or citations[i] != citations[i-1]:
            tmpCount = len(citations[i:])
        count.append(tmpCount)
        
        if citations[i] >= count[i]:
            return count[i]
    
    if isAllZero == True: return 0


# 불필요한 count = [] 삭제
# 불필요한 isAllZero 삭제 - for문 안에서 리턴되지 않으면
#   마지막에 0을 리턴하면 된다.
# 같은 횟수만큼 인용된 논문이 여러편인 경우 고려할 필요 없음
#   하단 예시를 참고
#   -> ci[i] != ci[i-1] 의 조건문 삭제
def solution_edit(citations):
    citations.sort()
    
    for i in range(len(citations)):
        if citations[i] >= len(citations[i:]):
            return len(citations[i:])
    
    return 0

citations = [0, 1, 2, 6, 7, 8]
print(solution_edit(citations))

'''
0 1 3 5 6
5 4 [3] 2 1
h = 3

0 1 2 6 7 8
6 5 4 [3] 2 1
h = 3

1 2 6 7 8 9
6 5 [4] 3 2 1
h = 4

0 1 1 1 1 2
6 5 5 5 5 [1]
h = 1 -> 이 경우, 모든 1이 필요없음

7 8 8 8 8 9
[6] 5 5 5 5 1
h = 6

3 8 8 8 8 9
6 [5] 5 5 5 1
h = 5 -> 이 경우, 첫번째 8 말고는 쓸모없음

0 0 0 0 0 0
6 6 6 6 6 6
'''