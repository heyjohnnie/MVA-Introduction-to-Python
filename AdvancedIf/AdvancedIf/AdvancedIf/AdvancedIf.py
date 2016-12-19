#Declare variables, and convert to float
totalOrderStr = input("Please input your total order: ")
shippingCOuntry = input("Plese type which country will be shipped the order: ").upper()
canadaProvince = " "
taxFee = 0
taxType = " "
totalOrder = float(totalOrderStr)

#evaluate country if canada, nested if defines province based taxation, else, it does not charges tax
if shippingCOuntry == "CANADA" :
    canadaProvince = input("Please, provide your province: ").upper()

    if canadaProvince == "ALBERTA" :
        taxFee = 0.0005
        taxType = "General Sales Tax"
        print("The total cost of the  {0:s}  order, plus a {1:s} of {2:.2f}% will be : {3:f}".format(totalOrderStr, taxType, taxFee * 100, totalOrder * (1 + taxFee)))

    elif canadaProvince == "ONTARIO" or canadaProvince == "NEW BRUNSWICK" or canadaProvince == "NOVA SCOTIA" :
        taxFee = 0.0013
        taxType = "Harmonized Sales Tax"
        print("The total cost of the  {0:s}  order, plus a {1:s} of {2:.2f}% will be : {3:f}".format(totalOrderStr, taxType, taxFee * 100, totalOrder * (1 + taxFee)))
    else :
        taxFee = 0.0011
        taxType = "combined Provincial Sales tax and General Sales Tax"
        print("The total cost of the  {0:s}  order, plus a {1:s} of {2:.2f}% will be : {3:f}".format(totalOrderStr, taxType, taxFee * 100, totalOrder * (1 + taxFee)))

else :
    print("Your total order will be: {0:f}".format(totalOrder))

