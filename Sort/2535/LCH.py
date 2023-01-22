n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[2], reverse=True)
if arr[0][0] == arr[1][0] and arr[1][0] == arr[2][0]:
    for i in range(3,n):
        if arr[i][0] != arr[0][0]:
            arr[2] = arr[i]
            break
for i in range(3):
    print(*arr[i][:2])
