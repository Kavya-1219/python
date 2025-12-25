print("enter a:")
a=int(input())
print("enter b:")
b=int(input())
print("non prime between ", a ,"& ",b," :" )
for x in range(a+1,b+1):
    if x>1:
        for i in range(2,x):
            if x%i==0:
                print(x)
                break