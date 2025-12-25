n=int(input("enter number of steps:"))
if n==1:
    print("num of ways:",1)
elif n==2:
    print("num of ways:",2)
else:
    a=1
    b=2
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
    print("num of ways:",c)