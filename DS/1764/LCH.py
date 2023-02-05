import sys 

n, m = map(int, sys.stdin.readline().split())
not_listen = set()
for i in range(n):
    not_listen.add(sys.stdin.readline())
ans = []
for i in range(m):
    not_seen = sys.stdin.readline()
    if not_seen in not_listen:
        ans.append(not_seen)
print(len(ans))
print("".join(sorted(ans)))
