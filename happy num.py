n=int(input("enter num:"))
temp=n
while temp!=1 and temp!=4:
    s=0
    while temp>0:
        d=temp%10
        s+=d**2
        temp=temp//10
    temp=s
    
if(temp==1):
    print(n," happy num")
else:
    print(n," not happy num")