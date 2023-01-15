import sys

n, k = map(int, input().split())
a = list(map(int, sys.stdin.readline().split()))
print(sorted(a)[k-1])
