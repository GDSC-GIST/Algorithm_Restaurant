n = int(input())
ans = 1
while n > 0:
    n -= ans
    ans += 1
print(ans)
