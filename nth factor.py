n=int(input("enter num:"))
nth=int(input("enter nth num:"))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
        if(count==nth):
            print(nth," factor of ",n," :",i)
print("num of factors:",count)