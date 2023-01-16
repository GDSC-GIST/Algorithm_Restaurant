import sys
input=sys.stdin.readline
arr=[]
for _ in range(int(input())):
  arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:x[2],reverse=True)

c=0
cnt={}
for e in arr:
  if c==3: 
    break
  elif e[0] not in cnt:
    print(*e[:2])
    cnt[e[0]]=1
    c+=1
  elif cnt[e[0]]<2:
    print(*e[:2])
    cnt[e[0]]+=1
    c+=1
