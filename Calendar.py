import calendar
yy=int(input("The year after 001 year:"))
mm=int(input("The months:"))
if mm in range(1,13):
    print(calendar.month(yy,mm)) #Command to show the data
else:
    print("Invalid Month")