import sys

firstNumberAsStr = input("Enter fist number: ")
secondNumberAsStr = input("Enter second number: ")
firstNumber = float(firstNumberAsStr)
secondNumber = float(secondNumberAsStr)

#If the code returns a syntax/runtime error, the except will handle it
try:
    result = firstNumber / secondNumber
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")
    sys.exit()

except:
    error = sys.exc_info()[0]
    print(error)

