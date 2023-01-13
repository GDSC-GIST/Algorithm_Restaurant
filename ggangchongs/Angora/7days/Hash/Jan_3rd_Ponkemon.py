import collections

def solution(nums):
    numsCounter = collections.Counter(nums)
    if len(numsCounter.keys()) >= len(nums)/2:
        return len(nums)/2
    else:
        return len(numsCounter.keys())


def solution_best(nums):
    return min(len(nums)/2, len(set(nums)))
# set 사용법에 익숙해져야 할 것 같다