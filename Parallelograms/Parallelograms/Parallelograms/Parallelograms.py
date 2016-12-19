import turtle

sidesAsString = input("Please, type the desired number of sides for the geometry: ")
sidesAsInt = int(sidesAsString)

for steps in range(sidesAsInt):
    turtle.forward(100)
    turtle.right(360/sidesAsInt)
    for moresteps in range (sidesAsInt):
        turtle.forward(50)
        turtle.right(360/sidesAsInt)