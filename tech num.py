n=int(input("enter num"))
s=str(n)
l=len(s)
if(l%2!=0):
    print(n," is not tech")
else:
    mid=l//2
    first=int(s[:mid])
    second=int(s[mid:])
    if (first+second)**2==n:
        print(n," is tech")
    else:
        print(n," is not tech")