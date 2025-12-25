l1=[1,2,4]
l2=[1,3,4]
merge=[]
for x in l1:
    merge.append(x)
for x in l2:
    merge.append(x)
merge.sort()
print(merge)