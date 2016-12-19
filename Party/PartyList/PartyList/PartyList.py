#Declaring variables and an empty list
guests = []
name = " "
#Set a flag for breaking the loop
endLoop = False

#While the flag remains false, the loop whill continue
while endLoop == False:
    name = input("Please, enter a gueste name, if non require, type 'DONE': ").upper()
    #The keyword for setting the flag is "DONE"
    if name == "DONE":
        endLoop = True
    else:
        guests.append(name)

#Sorting the guests and printing the results
guests.sort()
for singleGuest in guests:
    print(singleGuest)