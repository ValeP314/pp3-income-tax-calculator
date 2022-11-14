# This tax income calculator will ask some general information,
# in order to calculate the deductions applicable to our gross salary,
# and return annual and monthly net salary.


# print("What is your name?")
# full_name = input("Enter your full name here:\n")

print("Please type in your annual gross salary:")
gross_salary = int(input("Enter your annual gross salary here:\n"))

# print("Do you have any dependants?")
# dependants = input("True or False\n")

print("Do you contribute to any pension scheme?")
pension = int(input("Enter your annual contributions here:\n"))

taxable_salary = (gross_salary - pension)
print(f"Your taxable salary is {taxable_salary} €")

paye = 0
prsi = 0
usc = 0


def paye_taxes():
    global paye

    if taxable_salary < 36800:
        paye = taxable_salary * 0.20
        
    else:
        excess = taxable_salary - 36800
        first_band_paye_taxes = 36800 * 0.20
        paye = int(first_band_paye_taxes + (excess * 0.40))
    
    print(f"You pay {paye} € PAYE")
    return paye


def prsi_taxes():
    global prsi

    if gross_salary < 18304:
        prsi = 0
    else:
        prsi = int(gross_salary * 0.04)

    print(f"You pay {prsi} € PRSI")
    return prsi


def usc_taxes():
    global usc
    first_band = 12012
    second_band = first_band + 9283
    third_band = second_band + 48749

    if gross_salary < first_band:
        usc = int(gross_salary * 0.005)
    elif gross_salary < second_band:
        usc = int((first_band * 0.005) + ((gross_salary - first_band) * 0.02))
    elif gross_salary < third_band:
        usc = int((first_band * 0.005) + ((second_band - first_band) * 0.02) + ((gross_salary - second_band) * 0.045))   
    else:
        usc = int((first_band * 0.005) + ((second_band - first_band) * 0.02) + ((third_band - second_band) * 0.04) + ((gross_salary - third_band) * 0.08))

    print(f"You pay {usc} € USC")
    return usc


def calculate_total_taxes():
    total_taxes = int(paye) + int(prsi) + int(usc)
    print(f"You pay {total_taxes} € in taxes")
    net_pay = gross_salary - total_taxes
    print(f"You annual net pay is {net_pay} €")


def main():
    """
    Run all program functions
    """
    paye_taxes()
    prsi_taxes()
    usc_taxes()
    calculate_total_taxes()


main()