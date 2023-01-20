'''
heappush: logN
sort(): nlogn
max: n
remove: n
'''

def solution(operations):
    answer = []
    
    for op in operations:
        order, num = op.split()
        if order == 'I':
            answer.append(int(num))
        elif order == 'D' and len(answer) != 0:
            if int(num) == 1:
                tmpMax = max(answer)
                answer.remove(tmpMax)
            elif int(num) == -1:
                tmpMin = min(answer)
                answer.remove(tmpMin)
    
    if len(answer) == 0: return [0,0] # 비면 0 0
    else: # 안비면 max, min
        return [max(answer), min(answer)]

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations)) #[0,0]


# -------------------------------------- #
def solution_old(operations): # 못 풀었음
    minHq = []
    maxHq = []
    
    for op in operations:
        order, num = op.split()
        if order == 'I':
            hq.heappush(minHq, int(num))
            hq.heappush(maxHq, int(num)*(-1))
        elif order == 'D':
            if int(num) == 1 and len(maxHq) != 0:
                hq.heappop(maxHq)
            elif int(num) == -1 and len(minHq) != 0:
                hq.heappop(minHq)
                
    for i in range(len(maxHq)):
        maxHq[i] = -1*maxHq[i]
    
    intersection = list(set(minHq) & set(maxHq))
    if len(intersection) == 0: return [0,0]
    else:
        maxValue = max(intersection)
        minValue = min(intersection)
        return [maxValue, minValue]