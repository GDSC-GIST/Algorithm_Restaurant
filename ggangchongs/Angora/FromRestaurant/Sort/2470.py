import sys

n = int(sys.stdin.readline())
liquids = list(map(int,sys.stdin.readline().split()))
answer = []

liquids.sort()
# case1: all >= 0
if liquids[0] >= 0 and liquids[-1] >= 0:
    answer.append(liquids[0])
    answer.append(liquids[1])
# case2: all < 0
elif liquids[0] < 0 and liquids[-1] < 0:
    answer.append(liquids[-1])
    answer.append(liquids[-2])
# case3: + & -
else:
    list = sorted(liquids, key=lambda x : -abs(x))
    minResult = sys.maxsize
    minIndex = 0
    for i in range(len(list)-1):
        if minResult >= abs(list[i]+list[i+1]):
            minIndex = i
            minResult = abs(list[i]+list[i+1])
    answer.append(list[minIndex])
    answer.append(list[minIndex+1])

answer.sort()
print(str(answer[0]) + " " + str(answer[1]))


"""liquids = [0,0,0,0]
liquids = [1,2,3,4]
liquids = [-10, 1, 2]
#liquids = [-2,4,-99,-1,98]
#liquids = [999999995, 999999996, 999999997, 1000000000]
#liquids = [-99, -98, 1, 0, 96]
liquids = [-100, -99, 99, 1, 2, 3, 4, 5]"""