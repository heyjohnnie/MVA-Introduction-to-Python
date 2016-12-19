#def displayMessage(greeting, name):
#    message = greeting + ", " + name
#    print(message)
#    return

#displayMessage("Hi", "John")

def getMessage(name):
    message = "Hello, " + name
    return message

def printMessage(message):
    print(message)
    return

output = getMessage("John")
printMessage(output)