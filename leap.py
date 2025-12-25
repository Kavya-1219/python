date=input("enter date(dd/mm/yyyy):")
day,month,year=date.split("/")
y=int(year)
if (y%4==0 and y%100!=0)or (y%400==0):
    print("given year:","leap year")
    print("next anniversary:",day,"/",month,"/",str(y+1))
else:
    print("given year:","not leap year")
    print("previous anniversary:",day,"/",month,"/",str(y-1))