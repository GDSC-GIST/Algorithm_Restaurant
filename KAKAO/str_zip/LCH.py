def solution(s):
    answer = 99999
    if len(s) == 1:
        answer = 1
    for i in range(1, len(s) // 2 + 1):
        res = 0
        count = 1
        substr = s[:i]
        for j in range(1, len(s) // i + 1):
            if substr == s[i * j: i * (j+1)]:
                count += 1
            else:
                if count > 1:
                    res += len(str(count))
                res += i
                count = 1
                substr = s[i * j: i * (j+1)]
        res += len(s) % i
        answer = min(answer, res)
    return answer
