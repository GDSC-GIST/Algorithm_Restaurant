def solution(name):
    answer = 0
    
    minMove = len(name) - 1
    for i, char in enumerate(name):
        answer += min(ord(char) - 65, 90 - ord(char) + 1)
        # ord("A") = 65, ord("Z") = 90
        
        lastA = i + 1
        while lastA < len(name) and name[lastA] == "A":
            lastA += 1
        minMove = min(minMove,
                      2*i + len(name)-lastA,    # <-> AAAA <-
                      i + 2*(len(name)-lastA)   # -> AAAA <->
                      )
    
    answer += minMove
    return answer

# https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy