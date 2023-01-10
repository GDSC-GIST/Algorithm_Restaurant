import collections

def solution(participant, completion):
    result = collections.Counter(participant) - collections.Counter(completion)
    answer = list(result.keys())
    return answer[0]
    