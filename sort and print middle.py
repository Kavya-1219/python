n=int(input("enter num of elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("enter elements:")))
arr.sort()
print("sorted array:",arr)
print("mid element:",arr[n//2])