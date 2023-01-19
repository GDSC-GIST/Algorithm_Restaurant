n = int(input())
l = list(map(int, input().split()))
l.sort()

i = 0
j = n-1
val = 9999999999
ans1 = 0
ans2 = n-1
while i < j:
    liq = abs(l[i] + l[j])
    if liq < val:
        val = liq
        ans1 = l[i]
        ans2 = l[j]
    if liq == 0:
        break
    if liq < 0:
        i += 1
    else:
        j -= 1

print(ans1, ans2)
