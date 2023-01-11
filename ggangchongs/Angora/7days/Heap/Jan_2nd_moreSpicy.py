import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    first = heapq.heappop(scoville)
    while first < K:
        
        if len(scoville) == 0:
            answer = -1
            break
        
        answer += 1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville,
                       first + second*2)
        first = heapq.heappop(scoville)
    
    return answer

# edit
import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    
    first = hq.heappop(scoville)
    while first < K:
        
        if len(scoville) == 0:
            answer = -1
            break
        
        answer += 1
        second = hq.heappop(scoville)
        hq.heappush(scoville,
                       first + second*2)
        first = hq.heappop(scoville)
    
    return answer