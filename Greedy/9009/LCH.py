t = int(input())

fib = [1, 1]
i = 1
while fib[i] < 1000000000:
    fib.append(fib[i] + fib[i-1])
    i += 1
fib = fib[::-1]

for _ in range(t):
    n = int(input())
    ans = []
    for f in fib:
        if n >= f:
            ans.append(f)
            n -= f
    print(*ans[::-1])
