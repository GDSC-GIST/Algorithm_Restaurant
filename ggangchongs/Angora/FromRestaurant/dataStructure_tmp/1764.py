import sys

n, m = map(int, sys.stdin.readline().split())

d = []
for i in range(n): d.append(sys.stdin.readline())
b = []
for i in range(m): b.append(sys.stdin.readline())

db = sorted(list(set(d)&set(b)))
print(len(db))
for name in db:
    print(name, end='')