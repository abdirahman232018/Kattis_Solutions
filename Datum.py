
import datetime
day_month=input().split()

day, month, year = int(day_month[0]),int(day_month[1]),2009
ans = datetime.date(year, month, day)
print (ans.strftime("%A"))