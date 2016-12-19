#Variables required
ageInput = " "
fNameAsStr = " "
lNameAsStr = " "

#Create File and open it
demoFile = "list.csv"
WRITE = "w"
myFile = open(demoFile, mode = WRITE)

#Use while to loop user input and write into the file until done
while fNameAsStr != "DONE":
    fNameAsStr = input("Type first name, enter 'DONE' for exit: ").upper()
    if fNameAsStr != "DONE" :
        lNameAsStr = input("Type last name: ").upper()
        ageInput = input("Type age: " )
        myFile.write(fNameAsStr + ", " + lNameAsStr + ", " + ageInput + "\n")

#Close file and print message
myFile.close()
print("File succesfully created")