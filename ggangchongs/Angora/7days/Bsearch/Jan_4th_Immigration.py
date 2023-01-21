def solution(n, times):
    times.sort()
    start = 0
    end = times[0]*n
    
    while start <= end:
        mid = (start + end) // 2
        
        done = 0
        for t in times:
            done += mid // t
        
        if done >= n:
            end = mid -1
        elif done < n:
            start = mid + 1
            
    return start

n = 6
times = [7,10]
print(solution(n, times)) # 28
'''
7 10

1. setting
    1. start = 두번째 창구에서 전부 한다(첫번째 창구에서 아예 안함)
    2. end = 첫번째 창구에서 전부 한다
    
2. 이진 탐색 while문 조건: mid를 시간으로 설정했을 때, 피검사자의 수가 n인가?
    1. done 계산: mid를 넘지 않는 선에서, 최대로 받을 수 있는 피검사자의 수를 더한다.
    2. mid 변경: 정답 = **최소**이므로 count **<** m에 =을 붙인다.
3. return start (정답 = **최소)**
'''