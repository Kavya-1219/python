n=int(input("enter num:"))
num=int(input("enter how many factors of you want:"))
count=0
printed=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
        if printed<num:
            print(i)
            printed+=1
print("num of factors of ",n ,":",count)
