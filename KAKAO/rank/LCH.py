from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    database = {}
    lang = ["cpp", "java", "python", "-"]
    job = ["backend", "frontend", "-"]
    level = ["junior", "senior", "-"]
    food = ["chicken", "pizza", "-"]
    answer = []
    
    for l in lang:
        for j in job:
            for lvl in level:
                for f in food:
                    database["_".join([l, j, lvl, f])] = []
    
    for person in info:
        l, j, lvl, f, s = person.split()
        for i in range(5):
            c = list(combinations(range(4), i))
            for k in c:
                cases = [l, j, lvl, f]
                for r in k:
                    cases[r] = "-"
                database["_".join(cases)].append(int(s))
    for data in database:
        database[data].sort()
    
    for q in query:
        subq = q.replace('and', '').split()
        # binary search after sorting is cool!
        answer.append(len(database["_".join(subq[:-1])]) - bisect_left(database["_".join(subq[:-1])], int(subq[-1])))
    return answer
