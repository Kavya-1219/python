def simple_intrest(p,n,sc):
    if (g=="f" and sc=="y"):
        rate=15
    elif(g=="m" and sc=="y"):
        rate=12
    else:
        rate=10
    return (p*n*rate)/100
p=int(input("enter principle amount:"))
n=int(input("enter num of years:"))
sc=input("are you a senior citizen(y/n):")
g=input("gender(f/m):")
print("intrest=",int(simple_intrest(p,n,sc)))