def sumsquare(l):
    even=0
    odd=0
    for x in l:    
        if(x%2==0):
          even+=x*x
        else:
           odd+=x*x
    return[odd,even]
n=int(input("enter num of elements:"))
l=[]
for i in range(n):
   num=int(input("enter value:"))
   l.append(num)
print(sumsquare(l))