n=int(input("enter num:"))
temp=n
while temp>9:
    s=0
    while temp>0:
        d=temp%10
        s+=d
        temp=temp//10
    temp=s
    print(temp)