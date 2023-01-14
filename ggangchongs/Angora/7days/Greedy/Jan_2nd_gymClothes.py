def solution(n, lost, reserve):
    answer = 0
    
    clothes = [1 for i in range(n)]
    for i in lost:
        clothes[i-1] -= 1
    for i in reserve:
        clothes[i-1] += 1
    
    if clothes[0] == 2 and clothes[1] == 0:
        clothes[0], clothes[1] = 1,1
    for i in range(1, len(clothes)-1):
        if clothes[i] == 2:
            if clothes[i-1] == 0: clothes[i-1], clothes[i] = 1,1
            elif clothes[i+1] == 0: clothes[i], clothes[i+1] = 1,1
            else: continue
    if clothes[-1] == 2 and clothes[-2] == 0:
        clothes[-1], clothes[-2] = 1,1
    
    for i in clothes:
        if i == 0: answer += 1
    
    return n-answer


def solution_my_edit(n, lost, reserve):
    answer = 0
    
    clothes = [1 for i in range(n)]
    for i in lost:
        clothes[i-1] -= 1
    for i in reserve:
        clothes[i-1] += 1
    
    if clothes[0] == 2 and clothes[1] == 0:
        clothes[0], clothes[1] = 1,1
    for i in range(1, len(clothes)-1):
        if clothes[i] == 2:
            if clothes[i-1] == 0: clothes[i-1], clothes[i] = 1,1
            elif clothes[i+1] == 0: clothes[i], clothes[i+1] = 1,1
            else: continue
    if clothes[-1] == 2 and clothes[-2] == 0:
        clothes[-1], clothes[-2] = 1,1
    
    for i in clothes:
        if i == 0: answer += 1
    
    return n-answer

def solution_best(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)