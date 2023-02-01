def solution(clothes):
    
    type = {}
    for cloth in clothes:
        answer = 1
        if cloth[1] not in type:
            type[cloth[1]] = 1
        else:
            type[cloth[1]] += 1
    
    for c in type.values():
        answer *= c+1
    return answer-1


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))