n = int(input())
values = {}
for i in range(n):
    word = input()
    value = 1
    for char in word[::-1]:
        if char in values:
            values[char] += value
        else:
            values[char] = value
        value *= 10

sorted_values = sorted(values.items(), key=lambda x: x[1], reverse=True)
ans = 0
num = 9
for val in sorted_values:
    ans += num * val[1]
    num -= 1
print(ans)
