import sys

n = int(sys.stdin.readline())
timetable = []
for i in range(n):
    timetable.append(list(map(int, sys.stdin.readline().split())))

timetable = sorted(timetable, key=lambda x: (x[1],x[0]))
answer = 0
for i, lec in enumerate(timetable):
    if i == 0:
        end = lec[1]
        answer += 1
    else:
        if end <= lec[0]:
            answer += 1
            end = lec[1]
print(answer)