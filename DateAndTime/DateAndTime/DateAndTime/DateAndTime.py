#Import lib
import datetime

#Get current date
currentDate = datetime.date.today()
currentTime = datetime.datetime.now()

#Print the results and show its properties
print(currentDate)
print(currentDate.month)
print(currentDate.year)
print(currentDate.day)

print(currentTime)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)

#Apply format with strftime
print(currentDate.strftime("%A %d %b, %Y"))
print(currentTime.strftime("%H %M %S"))