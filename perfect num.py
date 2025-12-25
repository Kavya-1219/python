n=int(input("enter num:"))
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
if(n==s):
    print(n," is perfect num")
else:
    print(n," is not perfect num")