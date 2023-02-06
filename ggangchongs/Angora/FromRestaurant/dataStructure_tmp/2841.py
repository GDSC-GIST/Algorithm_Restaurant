import sys

n, p = map(int, sys.stdin.readline().split())
answer = 0

guitar = {}
line = 0
for i in range(n):
    newLine, newP = map(int, sys.stdin.readline().split())
    

    if line != newLine and newLine not in guitar:
        tmp = [newP]
        guitar[newLine] = tmp
        answer += 1
    elif (line != newLine and newLine in guitar) or line == newLine:
        tmp = guitar[newLine]
        while tmp[-1] > newP:
            tmp.pop(); answer += 1
            if len(tmp) == 0: break
        if len(tmp) == 0:
            tmp.append(newP)
            answer += 1
        elif tmp[-1] < newP:
            tmp.append(newP)
            answer += 1
        
    line = newLine             
    
print(answer)