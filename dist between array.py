n=int(input("enter num of elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("enter element:")))
arr.sort()
d=[]
for i in range(len(arr)-1):
    d.append(arr[i+1] - arr[i])
print(arr)
print(d)
