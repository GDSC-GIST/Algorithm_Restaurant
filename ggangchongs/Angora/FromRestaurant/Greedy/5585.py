import sys

n = int(sys.stdin.readline())
m = 1000-n

bill = [500,100,50,10,5,1]
answer = 0
for b in bill:
    if m < 0: break
    answer += m//b
    m = m%b

print(answer)