#Mortage calculator v1.0
loanAmount = input("Enter the total loan amount ")
interestRate = input("Enter the interest ")
numberOfPayments = input("Enter the total number of payments ")

#Converting to float
L = float(loanAmount)
i = float(interestRate)
n = float(numberOfPayments)

#Evaluating and printing the results with the proper format
monthlyPayment = L*((i*(1+i)*n)/((1+i)*n-1))
print("The monthly payment of the " + \
    "${0:.2f} loan at an interest rate of {1:.3f} for {2:.2f} months would be ${3:.2f} dollars".format(L, i, n, monthlyPayment))