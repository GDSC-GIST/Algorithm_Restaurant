def solution(n, lost, reserve):
    available = [False] * n
    solve = [0] * n
    for good in reserve:
        if good in lost:
            lost.remove(good)
            continue
        available[good-1] = True
    lost.sort()
    reserve.sort()
    for bad in lost:
        solve[bad-1] = -1
    for bad in lost:
        for good in reserve:
            if (bad+1 == good or bad-1 == good) and available[good-1] and solve[bad-1] == -1:
                available[good-1] = False
                solve[bad-1] = 0
    answer = n + sum(solve)
    return answer
