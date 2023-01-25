import os
import datetime
start_date =datetime.date(2021,2,6)
end_date = datetime.date(2021, 2, 10)
dateList = []
delta = datetime.timedelta(days=1)
while (start_date <= end_date):
    print(start_date, end="\n")
    dateList.append(start_date)
    start_date += delta
#print(dateList)
for i in dateList:
    print(i)
    dir = str(i)
    try:
        os.mkdir(dir)
        print ("Directory is created")
    except FileExistsError:
        print ("Directory already exists")
