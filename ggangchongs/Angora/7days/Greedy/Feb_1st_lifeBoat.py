def solution(people, limit):
    people = sorted(people, reverse=True)
    i,j = 0, len(people)-1
    answer = 0
    
    while i < j:
        tmp = people[i] + people[j]
        if tmp <= limit:
            while tmp + people[j-1] <= limit:
                tmp += people[j-1]
                j -= 1
            i += 1
            j -= 1
            answer += 1
        else:
            i += 1
            answer += 1
    if i == j: answer += 1
    
    return answer

people = [70, 50, 50, 10, 20]
limit = 100
print(solution(people, limit))