import turtle

#Define variable so loop can start
length = 1

#If a value of 0 in length is typed, the loop ends
while length > 0 :
    color = input("Color: ")
    lengthAsStr = input("Lenght: ")
    length = int(lengthAsStr)
    angleAsStr = input("Angle: ")
    angle = int (angleAsStr)
    turtle.color(color)
    turtle.right(angle)
    turtle.forward(length)
