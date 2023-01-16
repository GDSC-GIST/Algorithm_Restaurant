import sys
for _ in range(int(input())):
  n1=int(input())
  s1=set(map(int,input().split()))
  n2=int(input())
  for e in list(map(int,input().split())):
    if e in s1:
      print(1)
    else:
      print(0)
