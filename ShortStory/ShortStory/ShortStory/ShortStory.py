#This program creates a short story based on user's input

#Welcome message
print("Welcome to Story Teller v1.0")
print("Let's create a short story where you'll be the main character!")
print("First, we need some info about you")

#Getting data and making sure to correct the input
firstName = " "
firstName = input("What's your first name? ")
firstName = firstName.capitalize()

lastName = " "
lastName = input("What's your last name? ")
lastName = lastName.capitalize()

location = " "
location = input("Where are you from? ")
location = location.capitalize()

age = input("How old are you? ")

print("This is the story of " + firstName + ", from the " + lastName + " lineage, first of his name.")
print("Who at the age of " + age + ", became hero of the sacred realm of " + location + ".")