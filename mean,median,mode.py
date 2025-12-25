arr=[16, 18, 27, 16, 23, 21, 19]
arr.sort()
print(arr)
median=arr[len(arr)//2]
s=0
mcount=0
for x in arr:
    s+=x
mean=s/len(arr)
for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    if count>mcount:
        mcount=count
        mode=i
print(int(mean))
print(median)
print(mode)