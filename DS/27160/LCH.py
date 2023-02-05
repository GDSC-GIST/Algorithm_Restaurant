n = int(input())
fruits = {}
for i in range(n):
    fruit, amount = input().split()
    if fruit in fruits:
        fruits[fruit] += int(amount)
    else:
        fruits[fruit] = int(amount)
ans = "NO"
for amount in fruits.values():
    if amount == 5:
        ans = "YES"
print(ans)
