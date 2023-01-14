import sys

n = int(sys.stdin.readline())
candi = []
nationDict = {}
winner = []
for i in range(n):
    nation, num, score = map(int, sys.stdin.readline().split())
    candi.append([nation, num, score])

candi = sorted(candi, key = lambda x : (-x[2]))

i = 0
while len(winner) < 3:
    nationTmp = candi[i][0]
    if nationTmp in nationDict:
        if nationDict[nationTmp] == 1:
            nationDict[nationTmp] = 2
            winner.append([candi[i][0], candi[i][1]])
        # elif nationDict[nationTmp] == 2:
    else:
        nationDict[nationTmp] = 1
        winner.append([candi[i][0], candi[i][1]])
    i += 1

for i in winner:
    print (str(i[0]) + " " + str(i[1]))