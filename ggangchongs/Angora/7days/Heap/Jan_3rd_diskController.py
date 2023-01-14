import heapq

def solution(jobs):
    answer = 0
    jobs = sorted(jobs, key = lambda x : (x[0], x[1]))
    num = len(jobs)
    
    working = heapq.heappop(jobs)
    answer += 0 + working[1]
    nowTime = working[0] + working[1]
    waitingHeap = []
    notyet = []
    
    while len(jobs) != 0:
        waitingHeap.clear()
        notyet.clear()
        for j in jobs:
            if j[0] <= nowTime:
                heapq.heappush(waitingHeap, [j[1],j[0]])
            else: heapq.heappush(notyet, j)
        
        if len(waitingHeap) != 0:
            working = heapq.heappop(waitingHeap)
            answer += nowTime + working[0] - working[1]
            nowTime += working[0]
        else:
            working = heapq.heappop(notyet)
            answer += working[1]
            nowTime = working[0] + working[1]
        
        for i in range(len(waitingHeap)):
            waitingHeap[i] = [waitingHeap[i][1], waitingHeap[i][0]]
        jobs = waitingHeap + notyet
        
    return int(answer/num)

jobs = [[2, 6], [0, 3], [1, 9]]
print(solution(jobs))