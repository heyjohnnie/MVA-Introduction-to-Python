#Area of a triangle

#Declaring numeric variables
area = 0
height = 10
width = 20

area = width * height/2

#Strings do not concatenate with numbers
print("The area of the triangle would be %d square units" % area)
area = width * height

#Using position format
print("The area of a {0:d} width" + \
    "and {1:d} height rectangle would be {2:d} square units".format(width, height, area))