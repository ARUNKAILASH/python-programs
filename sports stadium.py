s,n,k,m=map(int,input().split(','))
l=list(map(int,input().split(',')))
d=n-k
w=k
a=[]
for i in range(m):
    d=n-k
    w=k
    for j in range(i,m):
        if(d<=0 and w<=0):
            break
        if(sum(l[i:m])<k):
            break
        if(j%2==1 and w==0):
            if(l[j]>=15):
                break
        if(j%2==1):
            w=w-l[j]
        if(j%2==0):
            d=d-l[j]
            if(d<0):
                r=d   
    if(d>0):
        continue
    a.append(sum(l[i:j])+r)
print(min(a)-1)
    
