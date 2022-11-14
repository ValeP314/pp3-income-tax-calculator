# This tax income calculator will ask some general information
# in order to calculate the deductions applicable to our gross salary,
# and return annual and monthly net salary.


#print("What is your name?")
#full_name = input("Enter your full name here:\n")
print("Please type in your annual gross salary:")
gross_salary = int(input("Enter your annual gross salary here:\n"))
#print("Do you have any dependants?")
#dependants = input("True or False\n")
print("Do you pay any pension?")
pension = int(input("Enter your annual gross salary here:\n"))
    
taxable_salary = (gross_salary - pension)


def taxes():
    if taxable_salary < 36800:
        tax = taxable_salary * 0.20
    
    else:
        excess = taxable_salary - 36800
        first_band_taxes = 36800 * 0.20
        tax = first_band_taxes + (excess * 0.40)
    
    print(f"You pay {tax} €")


def main():
    """
    Run all program functions
    """
    taxes()
    

main()