n = int(input())
alpha = {}
for i in range(n):
    voca = list(input())
    length = len(voca)
    for i in range(length):
        if voca[i] not in alpha:
            alpha[voca[i]] = 10**(length-(i+1))
        else:
            alpha[voca[i]] += 10**(length-(i+1))

sorted_alpha = sorted(alpha.items(), key = lambda item: -item[1])
start = 9
answer = 0
for a, count in sorted_alpha:
    answer += start*count
    start -= 1
print(answer)