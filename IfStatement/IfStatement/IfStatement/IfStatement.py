#Import locale to get the currency format
import locale
locale.setlocale( locale.LC_ALL, '')

#Declaring values
shippingFee = 10
freeShipping = False

#A float input is required
shoppingTotal = float(input("Please, enter the total amount of your purchase: "))

#Using boolen to flag the shipping condition
if shoppingTotal > 50 :
    freeShipping = True

#If the total purchase is greater than 50, the shipping cost goes free
if freeShipping :
    print("Your purchase applies for free shipping")
    shippingFee = 0

else :
    print("A $10 shipping fee will be charged")

#Printing results, no additional variable is needed
print("Your total order, including shipping, would be " + locale.currency(shippingFee + shoppingTotal))