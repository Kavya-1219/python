n=int(input("enter rows:"))
for i in range(n,0,-1):
    print(" " * (n-i) + "*" * i)