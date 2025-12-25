num=int(input("enter num:"))
temp=num
n=len(str(num))
s=0
while temp>0:
    d=temp%10
    s+=d**n
    temp=temp//10
if(s==num):
    print(num," is armstrong")
else:
    print(num," is not armstrong")