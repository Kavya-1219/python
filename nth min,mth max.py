arr=[14,16,87,36,25,89,34]
m=1
n=3
arr.sort()
if m<=0 or n<=0 or m>len(arr) or n>len(arr):
    print("invalid m or n")
else:
    M=arr[-m]
    N=arr[n-1]
    print("mth max",M)
    print("nth min:",N)
    print("sum:",M+N)
    print("difference:",M-N)
    print("product",M*N)
