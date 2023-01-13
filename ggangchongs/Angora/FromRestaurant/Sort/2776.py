import sys

T = int(sys.stdin.readline())

for i in range(T):
    note1Num = int(sys.stdin.readline())
    note1 = list(map(int, sys.stdin.readline().split()))
    note1.sort()
    note2Num = int(sys.stdin.readline())
    note2 = list(map(int, sys.stdin.readline().split()))

    note2edit = []
    for i in range(len(note2)):
        note2edit.append([note2[i], i, 0])
    note2edit = sorted(note2edit, key = lambda x : (x[0]))

    j = 0
    for i in range(len(note2edit)):
        while j < len(note1):
            if note2edit[i][0] == note1[j]:
                note2edit[i][2] = 1
                break
            elif note2edit[i][0] < note1[j]: break
            else:
                j += 1

    note2edit = sorted(note2edit, key = lambda x : (x[1]))
    for i in note2edit:
        print(i[2])

'''
1
5
4 1 5 2 3
5
1 3 7 9 5


'''