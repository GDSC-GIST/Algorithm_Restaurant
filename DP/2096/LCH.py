n = int(input())
maxDP = [0] * 3
minDP = [0] * 3
for i in range(n):
    a, b, c = map(int, input().split())
    maxDP = [a + max(maxDP[0], maxDP[1]), b + max(maxDP), c + max(maxDP[1], maxDP[2])]
    minDP = [a + min(minDP[0], minDP[1]), b + min(minDP), c + min(minDP[1], minDP[2])]

print(max(maxDP), min(minDP))
