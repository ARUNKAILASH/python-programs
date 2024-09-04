'''bank=[]
principal=int(input())
years=int(input())
for i in range(0,2):
    installments=int(input())
    sum=0
    for i in range(0,installments):
        time,r=[float(i) for i in input().split()]
        sq=1+pow((r),time*12)
        emi=((principal*r)/(1-1/sq))
        sum=sum+emi
    bank.append(sum)
if bank[0]<bank[1]:
    print("Bank A")
else:
    print("Bank B")'''
time,r=[float(i) for i in input().split()]
        
