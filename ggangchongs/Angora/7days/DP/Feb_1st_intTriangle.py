def solution(triangle):
    higher = triangle[0]
    
    for i in range(1, len(triangle)):
        now = triangle[i]
        for j in range(len(now)):
            if j == 0: now[j] += higher[0]
            elif j == len(now)-1: now[j] += higher[j-1]
            else: now[j] += max(higher[j-1], higher[j])
        higher = now
    
    return max(higher)