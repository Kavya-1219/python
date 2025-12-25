n=int(input("enter num:"))
temp=n
s=0
while temp>0:
    d=temp%10
    s+=d
    temp=temp//10
if(n%s==0):
    print(n," is harshad/niven num")
else:
    print(n," is not harshad/niven num")