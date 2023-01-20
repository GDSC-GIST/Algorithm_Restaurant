n = int(input())
voca = []
alpha = {}
for i in range(n):
    tmp = list(input())
    for t in tmp:
        alpha[t] = 0
    voca.append(tmp)

for v in voca:
    length = len(v)
    for i in range(length):
        oldValue = alpha[v[i]]
        alpha[v[i]] += 10**(length-(i+1))

sorted_alpha = sorted(alpha.items(), key = lambda item: -item[1])
start = 9
answer = 0
for a, count in sorted_alpha:
    answer += start*count
    start -= 1
print(answer)