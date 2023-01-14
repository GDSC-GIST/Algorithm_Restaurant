def solution(participant, completion):
    answer = ''
    hash = {}
    for i in participant:
        if i in hash: hash[i] += 1
        else: hash[i] = 1
    for i in completion:
        if i in hash: hash[i] -= 1
    answer = [k for k, v in hash.items() if v != 0]    
    return answer[0]


import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''
Counter 생성자는 중복된 데이터가 저장된 배열을 인자로 넘기면 -> 각 원소가 몇 번씩 나오는지가 저장된 객체를 얻게 됩니다.
>>> Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
Counter({'hi': 3, 'hey': 2, 'hello': 1})
+) 빼기도 가능!
'''