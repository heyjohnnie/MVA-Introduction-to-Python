#Import library
import csv

#Define constant
READ = "r"

#Open file more securely
with open("list.csv", READ) as myCSVFile:
    #Create list from file
    rowFromFile = csv.reader(myCSVFile)
    #Print each value without brackets
    for row in rowFromFile:
        print(", ".join(row))
