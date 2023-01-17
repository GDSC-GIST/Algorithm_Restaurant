def solution(N, number):
    
    if N == number: return 1

    result = [[0], [N]]    
    for i in range(2,9):
        # 0,1의 경우는 미리 삽입
        # 8개로 만들 수 없으면 -1을 리턴, 8까지만 계산
        tmp_result = []
        tmp_result.append(int(str(N)*i))
        for j in range(1, i//2+1):
            # ex. 5 = 4+1 = 3+2, 까지만 하면 된다
            for first in result[j]:
                for second in result[i-j]:
                    if first+second > 0 and first+second not in tmp_result:
                        tmp_result.append(first+second)
                    if first-second > 0 and first-second not in tmp_result:
                        tmp_result.append(first-second)
                    if first*second > 0 and first*second not in tmp_result:
                        tmp_result.append(first*second)
                    if first//second > 0 and first//second not in tmp_result:
                        tmp_result.append(first//second)
                    
                    if second-first > 0 and second-first not in tmp_result:
                        tmp_result.append(second-first)
                    if second//first > 0 and second//first not in tmp_result:
                        tmp_result.append(second//first)
                    
                    if number in tmp_result: return i
        result.append(tmp_result)
    # 8번 다 돌 때까지 number가 나타나지 않았으면 -1리턴
    return -1

print(solution(5,12)) # 4

'''
for i in range(2, 9):
    lst = [int(str(N)*i)]
로 초기화하는 것도 방법일 듯
'''