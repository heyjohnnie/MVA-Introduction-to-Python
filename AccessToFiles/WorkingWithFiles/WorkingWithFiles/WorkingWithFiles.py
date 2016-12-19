fileName = "demo.txt"
WRITE = "w"

myFile = open(fileName, mode = WRITE)
myFile.write("Hello World!")
myFile.close()