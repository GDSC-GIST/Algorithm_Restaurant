def solution(array, commands):
    answer = []
    for c in commands:
        answer.append(getAnswer(array, c[0], c[1], c[2]))
    return answer

def getAnswer(array, first, last, index):
    tmpArray = array[first-1:last]
    tmpArray.sort()
    return tmpArray[index-1]


def solution_best(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    # (lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands)
    # 각 x에 대해 sorted(array[x[0]-1:x[1]])[x[2]-1]를 진행
        # = getAnswer(array, x[0], x[1], x[2])
        # +) x는 `for x in commands`와 같음.
    # 해당 값들을 list형식으로 mapping 후 리턴
    
    # 각 기능에 따라 함수를 분리하는 것은 프로그래밍에서 중요한 것이고,
    # 코딩테스트의 특성상 함수 분리보다는 코드의 간결함이 우선인가? 잘 모르겠다