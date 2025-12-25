n=int(input("enter a num:"))
temp=n
rev=0
while temp>0:
    d=temp%10
    rev=rev*10+d
    temp=temp//10
if n==rev:
    print("palindrome")
else:
    print("not palindrome")