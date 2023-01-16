import sys
input()
a=[] #+
b=[] #-
for e in sorted(map(int,input().split())):
  if e<0:
    b.append(e)
  else:
    a.append(e)

b=b[::-1]
min_val=2000000000
rst=0,0
i,j=0,0
while i<len(a) and j<len(b):
  if min_val>abs(a[i]+b[j]):
    min_val=abs(a[i]+b[j])
    rst=b[j],a[i]
  if a[i]<-b[j]:
    i+=1
  elif a[i]==-b[j]:
    rst=b[j],a[i]
    break
  else:
    j+=1

if len(b)>1 and min_val>-(b[0]+b[1]):
  rst=b[1],b[0]
if len(a)>1 and min_val>a[0]+a[1]:
  rst=a[0],a[1]

print(rst[0],rst[1])
