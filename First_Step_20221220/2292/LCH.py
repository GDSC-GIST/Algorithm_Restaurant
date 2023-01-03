n = int(input()) - 1
ans = 1

while(n > 0):
    n -= ans * 6
    ans += 1

print(ans)
