n=int(input("enter matrix size:"))
m=[]
print("enter matrix elements:")
for i in range(n):
    m.append(list(map(int,input().split())))
    
print(m)