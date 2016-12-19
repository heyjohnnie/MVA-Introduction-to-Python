
WRITE = "w"

def getUserInput(fileInput, fileName):
    file = open(fileName, WRITE)
    file.write(fileInput)
    file.close()
    return

userInputName = input("Write the file name as .txt: ")
userInputData = input("Input data: ")

getUserInput(userInputData, userInputName + ".txt")