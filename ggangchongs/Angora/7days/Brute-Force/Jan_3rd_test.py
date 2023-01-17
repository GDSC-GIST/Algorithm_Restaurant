def solution(answers):
    winner = []
    score = [[0,1], [0,2], [0,3]]
    answerList = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    answerIndex = [0,0,0]
    indexLimit = [5, 8, 10]
    for i in answers:
        for j in range(3):
            if i == answerList[j][answerIndex[j]]:
                score[j][0] += 1
            answerIndex[j] += 1
            if answerIndex[j] == indexLimit[j]:
                answerIndex[j] = 0
    
    score.sort(reverse=True)
    maxScore = 0
    for i in range(3):
        if score[i][0] >= maxScore:
            maxScore = score[i][0]
            winner.append(score[i][1])
    winner.sort()
    
    return winner

answers = [2, 1, 2, 3, 2, 4, 2, 5]
print(solution(answers))


# enumerate & idx%len(pattern1)
def solution_best(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result