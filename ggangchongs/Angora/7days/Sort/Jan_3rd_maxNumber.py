def solution(numbers):
    
    answer = ""
    numEdit = []
    for i in range(len(numbers)):
        tmpLen = len(str(numbers[i]))
        tmpMulti = (str(numbers[i])*4)[:4]
        numEdit.append( (tmpMulti, tmpLen) )
    
    isZero = True
    numEdit.sort(reverse=True)
    for i in range(len(numEdit)):
        tmp = (numEdit[i][0])[:numEdit[i][1]]
        if tmp != "0": isZero = False
        answer += tmp
        
    if isZero == True:
        answer = "0"
    return answer


def solution_best(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

'''
numbers의 원소는 0 이상 1,000 이하
- 반복하게 되면, 빈 자리가 맨 첫번째 수로 채워진다.
    -> 비교할 때 30 3 => 30 33 => 3 > 30 으로 정렬 가능
    -> 전체적으로 반복하는 것이 좋음
    cf. 303, 30에 맨 앞자리를 다 붙이면 3033, 3033 으로 같다.
- 최대 길이수가 4개(1000)이기 때문에, 그냥 최대 길이인 4개까지 반복한다.
- 가장 짧은 1자리 수가 4자리수가 되려면 4번 반복해야함. 
'''