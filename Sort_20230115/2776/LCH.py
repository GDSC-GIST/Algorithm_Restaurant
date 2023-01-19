t = int(input())
while t:
    n = int(input())
    mem = map(int, input().split())
    table = {}
    for num in mem:
        table[num] = 1
    m = int(input())
    test = map(int, input().split())
    for tnum in test:
        if tnum in table:
            print(1)
        else:
            print(0)
    
    t -= 1
