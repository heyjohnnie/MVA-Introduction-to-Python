import datetime

#Int types are required to use operators with time
finalDate = " "
remainingDays = 0
remainingWeeks = 0
finalDays = 0

currentDate = datetime.date.today()

finalDate = input("Please, enter the final date of completition mm/dd/yyyy ")
deadLine = datetime.datetime.strptime(finalDate, "%m/%d/%Y").date()

#The .days property will return an integrer and the // operator returns the division without remainder
remainingDays = deadLine - currentDate
remainingWeeks = remainingDays.days // 7
finalDays = remainingDays.days%7

#Usinf the format property, the results can be printed as integrers
print("You have {0:d} weeks and {1:d} days left until your deadline!".format(remainingWeeks, finalDays))