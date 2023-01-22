n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
print("\n".join(list(map(str, sorted(arr)))))
