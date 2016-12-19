import datetime

currentDay = datetime.date.today()

userInput = input("What is yout birthday (mm/dd/yyyy? ")
birthday = datetime.datetime.strptime(userInput, "%m/%d/%Y").date()
print(birthday)

remainingDays = birthday - currentDay
print(remainingDays.days)