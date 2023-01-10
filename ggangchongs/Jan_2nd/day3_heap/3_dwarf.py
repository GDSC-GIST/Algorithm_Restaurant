import heapq

def solution(scoville, K):
    if scoville:
        heapq.heapify(scoville)
    istrue = False
    count = 0
    while scoville:
        test = heapq.heappop(scoville)
        if test >= K:
            istrue = True
            break
        elif not scoville:
            break
        heapq.heappush(scoville, test)
        fir = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)
        mixed = fir + (sec * 2)
        count = count + 1
        heapq.heappush(scoville, mixed)
        
    if istrue:
        answer = count
    else:
        answer = -1
    return answer
