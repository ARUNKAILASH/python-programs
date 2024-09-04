T=int(input())
n=int(input())
m=list(map(int,input().split(',')))
c=ord('a')
l=[]
r=[]
k=[]
for i in range(n):
    l.append(chr(c+i))
k=l.copy()
r=l.copy()
j=0
while(1):
    for i in range(n):
        l[m[i]-1]=k[i]
    k=l.copy()
    if(k!=r):
        i+=1
    else:
        break
print(i+1)
        


