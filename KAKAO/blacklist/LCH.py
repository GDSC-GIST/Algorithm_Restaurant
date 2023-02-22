from itertools import permutations


def check(uid, reg):
    if len(uid) != len(reg):
        return False
    
    for i in range(len(uid)):
        if reg[i] == "*":
            continue
        if uid[i] != reg[i]:
            return False
        
    return True


def solution(user_id, banned_id):
    answer = set()
    for uids in permutations(user_id, len(banned_id)):
        for i in range(len(banned_id)):
            if not check(uids[i], banned_id[i]):
                break
        else:
            answer.add(str(sorted((uids))))
    return len(answer)
