a = []
ans = ""

for _ in range(5):
    a.append(input())

max_len = max([len(x) for x in a])

for i in range(max_len):
    for s in a:
        if i < len(s):
            ans += s[i]

print(ans)
