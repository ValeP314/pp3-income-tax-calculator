# This tax income calculator will ask some general information,
# in order to calculate the deductions applicable to our gross salary,
# and return annual, monthly and weekly net salary,
# based on 2022 or 2023 Budget.

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('tax_income_calculator')

parameters_worksheet = SHEET.worksheet('parameters')


def select_year(year_input):

    # print("Please select the taxable year:")
    # year_input = int(input("Enter 2022 0r 2023\n"))

    # taxable_year = year_input

    if year_input == 2022:
        ref_cell = 2
    elif year_input == 2023:
        ref_cell = 3

    # return cell


def tax_credits(marital_status, ref_cell):
    """
    Calculates the tax credits according to marital status and dependants
    """
    if marital_status == 1:
        credit = (parameters_worksheet.cell(ref_cell, 7).value +
                 (parameters_worksheet.cell(ref_cell, 9).value) +
                 (parameters_worksheet.cell(ref_cell, 10).value))
        return ref_cell

    elif marital_status == 2:
        credit = (parameters_worksheet.cell(ref_cell, 8).value +
                  parameters_worksheet.cell(ref_cell, 10).value)
        return ref_cell
        
    elif marital_status == 3:
        credit = (parameters_worksheet.cell(ref_cell, 8).value +
                  parameters_worksheet.cell(ref_cell, 10).value)
        return ref_cell
        
    elif marital_status == 4:
        credit = (parameters_worksheet.cell(ref_cell, 7).value +
                 parameters_worksheet.cell(ref_cell, 10).value)
        return ref_cell

    else:
        credit = 0
        print("The status input is not valid.")
        return ref_cell

    print("")
    print(f"Your tax credits are {credit}€")
    return credit


def paye_taxes(taxable_salary, credit, ref_cell):
    """
    Calculates the "Pay As You Earn" taxes applicable to the taxable salary
    """
    # cell = int(cell)
    paye_year = int(parameters_worksheet.cell(ref_cell, 2).value)

    if taxable_salary < paye_year:
        paye = taxable_salary * 0.20
    else:
        excess_paye = taxable_salary - paye_year
        first_band_paye_taxes = paye_year * 0.20
        paye = (first_band_paye_taxes + (excess_paye * 0.40))
    paye = paye - credit
    print("")
    print("-----------------------------------------------------------------")
    print("")
    print(f"PAYE = {paye}€")
    return paye, ref_cell


def prsi_taxes(gross_salary, ref_cell):
    """
    Calculates the PRSI taxes applicable to the gross salary
    """

    prsi_year = int(parameters_worksheet.cell(cell, 3).value)

    if gross_salary < prsi_year:
        prsi = 0
    else:
        prsi = int(gross_salary * 0.04)

    print(f"PRSI = {prsi}€")

    return prsi, ref_cell


def usc_taxes(gross_salary, ref_cell):
    """
    Calculates the Universal Social Charge, applicable to the gross salary
    """

    usc_1_band = int(parameters_worksheet.cell(ref_cell, 4).value)
    usc_2_band = int(parameters_worksheet.cell(ref_cell, 5).value)
    usc_3_band = int(parameters_worksheet.cell(ref_cell, 6).value)

    if gross_salary < 13000:
        usc = 0
    elif gross_salary < usc_2_band:
        usc = int((usc_1_band * 0.005) + ((gross_salary - usc_1_band) * 0.02))
    elif gross_salary < usc_3_band:
        usc = int((usc_1_band * 0.005) +
                  ((usc_2_band - usc_1_band) * 0.02) +
                  ((gross_salary - usc_2_band) * 0.045))
    else:
        usc = int((usc_1_band * 0.005) +
                  ((usc_2_band - usc_1_band) * 0.02) +
                  ((usc_3_band - usc_2_band) * 0.045) +
                  ((gross_salary - usc_3_band) * 0.08))

    print(f"USC = {usc}€")

    return usc, ref_cell


def calculate_total_taxes(paye_calc, prsi_calc, usc_calc, credit_calc,
                          gross_salary):
    """
    Adds the 3 contributions in order to calculate annual, monthly
    and weekly net pay
    """
    total_taxes = int(paye_calc[0] + prsi_calc[0] + usc_calc[0] -
                      credit_calc[0])
    print(f"You pay a total of {total_taxes}€ in taxes")
    print("")
    print("-----------------------------------------------------------------")
    print("")
    net_pay = gross_salary - total_taxes
    print(f"Your annual net pay is {net_pay}€")
    print("")
    monthly_pay = int(net_pay / 12)
    print(f"Your monthly net pay is {monthly_pay}€")
    print("")
    weekly_pay = int(net_pay / 52)
    print(f"Your weekly net pay is {weekly_pay}€")


def main():
    """
    Runs all program functions
    """
    # parameters_worksheet = SHEET.worksheet('parameters')

    credit = 0
    paye = 0
    prsi = 0
    usc = 0

    print("")
    print("=================================================================")
    print("Welcome to the Irish Tax Income Calculator")
    print("=================================================================")
    print("")

    while True: 
        print("Please select the taxable year:")
        year_input = input("Enter 2022 or 2023\n").strip()

        if year_input not in ['2022', '2023']:
            print("Please enter 2022 or 2023.")
            continue

        else:
            break

    while True:    
        print("Please type in your annual gross salary:")
        gross_salary = input("Enter your annual gross salary here:\n").strip()
        
        if not gross_salary.isdigit():
            print("Please enter a number.")
            continue

        else:
            gross_salary = int(gross_salary)
            break

    while True:
        print("What is your marital status?")
        print("Please type in 1 for single.")
        print("Please type in 2 for married on one income.")
        print("Please type in 3 for married on two incomes.")
        print("Please type in 4 for single with dependants.")
        marital_status = input("Enter your marital status here:\n")

        if marital_status not in ['1', '2', '3', '4']:
            print("Please enter 1, 2, 3 or 4.")
            continue

        else:
            break


    # print("Do you have any dependants?")
    # dependants = input("True or False\n")

    while True: 
        print("Do you contribute to any pension scheme?")
        pension = input("Enter your annual contributions here:\n")

        if not pension.isdigit():
            print("Please enter a number.")
            continue

        else:
            pension = int(pension)
            break

    taxable_salary = (gross_salary - pension)

    ref_cell = select_year(year_input)

    print("")
    print("-----------------------------------------------------------------")
    print("")
    print(f"Your annual gross salary in {year_input} is {gross_salary}€")
    print("")
    print(f"Your annual pension contribution is {pension}€")
    print("")
    print(f"Your taxable salary is {taxable_salary}€")
    print("")
    # tax_credits(marital_status, dependants, cell)
    credit_calc = tax_credits(marital_status, ref_cell)
    # paye_taxes(taxable_salary, cell)
    paye_calc = paye_taxes(taxable_salary, credit, ref_cell)
    print("")
    # prsi_taxes(gross_salary, cell)
    prsi_calc = prsi_taxes(gross_salary, ref_cell)
    print("")
    # usc_taxes(gross_salary, cell)
    usc_calc = usc_taxes(gross_salary, ref_cell)
    print("")
    total_taxes = calculate_total_taxes(paye_calc, prsi_calc, usc_calc,
                                        credit_calc, gross_salary)
    print("")
    print("=================================================================")


main()


# if __name__ == '__main__':
#     main()
