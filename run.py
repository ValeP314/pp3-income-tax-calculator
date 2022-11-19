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
    ref_row = 2

    if year_input == '2022':
        valid_row = 2
    elif year_input == '2023':
        valid_row = 3
    return valid_row


def tax_credits(marital_status, valid_row, credit, year_input):
    """
    Calculates the tax credits according to marital status and dependants
    """
    valid_row = select_year(year_input)

    if marital_status == "1":
        credit = (int(parameters_worksheet.cell(valid_row, 7).value) +
                  int(parameters_worksheet.cell(valid_row, 10).value))

    elif marital_status == "2":
        credit = (int(parameters_worksheet.cell(valid_row, 8).value) +
                  int(parameters_worksheet.cell(valid_row, 10).value))

    elif marital_status == "3":
        credit = (int(parameters_worksheet.cell(valid_row, 7).value) +
                  int(parameters_worksheet.cell(valid_row, 9).value) +
                  int(parameters_worksheet.cell(valid_row, 10).value))

    print("")
    print(f"Your tax credits are {credit}€")
    return credit


def paye_taxes(taxable_salary, credit, valid_row, year_input):
    """
    Calculates the "Pay As You Earn" taxes applicable to the taxable salary
    """
    valid_row = select_year(year_input)
    paye_year = int(parameters_worksheet.cell(valid_row, 2).value)

    if taxable_salary < paye_year:
        paye = taxable_salary * 0.20
    else:
        excess_paye = taxable_salary - paye_year
        first_band_paye_taxes = paye_year * 0.20
        paye = (first_band_paye_taxes + (excess_paye * 0.40))

    paye = int(paye)

    print("")
    print("-----------------------------------------------------------------")
    print("")
    print(f"PAYE = {paye}€")

    return paye


def prsi_taxes(gross_salary, valid_row, year_input):
    """
    Calculates the PRSI taxes applicable to the gross salary
    """
    valid_row = select_year(year_input)
    prsi_year = int(parameters_worksheet.cell(valid_row, 3).value)

    if gross_salary < prsi_year:
        prsi = 0
    else:
        prsi = int(gross_salary * 0.04)

    print(f"PRSI = {prsi}€")

    return prsi


def usc_taxes(gross_salary, valid_row, year_input):
    """
    Calculates the Universal Social Charge, applicable to the gross salary
    """
    valid_row = select_year(year_input)

    usc_1_band = int(parameters_worksheet.cell(valid_row, 4).value)
    usc_2_band = int(parameters_worksheet.cell(valid_row, 5).value)
    usc_3_band = int(parameters_worksheet.cell(valid_row, 6).value)

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

    return usc


def calculate_total_taxes(paye, prsi, usc, credit,
                          taxable_salary):
    """
    Adds the 3 contributions in order to calculate annual, monthly
    and weekly net pay
    """

    total_taxes = int(paye + prsi + usc - credit)

    print(f"Deducting tax credits, you pay a total of {total_taxes}€ in taxes")
    print("")
    print("-----------------------------------------------------------------")
    print("")
    net_pay = taxable_salary - total_taxes
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
    ref_row = 2
    credit = 0
    paye = 0
    prsi = 0
    usc = 0

    print("")
    print("=================================================================")
    print("Welcome to the Irish Tax Income Calculator")
    print("=================================================================")
    print("")

    # Ask to select the relevant tax year and validate input
    # according to taxable year
    while True:
        print("Please select the taxable year:")
        year_input = input("Enter 2022 or 2023\n").strip()

        if year_input not in ['2022', '2023']:
            print("Please enter 2022 or 2023.")

            continue

        else:
            break

    # Ask about annual gross salary and validate numerical input
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
        print("Please type in 1 for single without dependants.")
        print("Please type in 2 for married on one or two income(s).")
        print("Please type in 3 for single with dependants.")
        marital_status = input("Enter your marital status here:\n").strip()

        if marital_status not in ['1', '2', '3']:
            print("Please enter 1, 2 or 3")
            continue

        else:
            break

    # Ask about pension contributions and validate numerical input
    while True:
        print("Do you contribute to any pension scheme?")
        pension = input("Enter your annual contributions here:\n").strip()

        if not pension.isdigit():
            print("Please enter a number.")
            continue

        else:
            pension = int(pension)
            break

    # Calculate taxable salary
    taxable_salary = (gross_salary - pension)

    # Call select_year function
    valid_row = select_year(year_input)

    # Print general information
    print("")
    print("-----------------------------------------------------------------")
    print("")
    print(f"Your annual gross salary in {year_input} is {gross_salary}€")
    print("")
    print(f"Your annual pension contribution is {pension}€")
    print("")
    print(f"Your taxable salary is {taxable_salary}€")
    print("")

    # Call tax_credit function
    credit_calc = tax_credits(marital_status, ref_row, credit, year_input)

    # Call paye_taxes function
    paye_calc = paye_taxes(taxable_salary, credit, ref_row, year_input)
    print("")

    # Call prsi_taxes function
    prsi_calc = prsi_taxes(gross_salary, ref_row, year_input)
    print("")

    # Call usc_taxes function
    usc_calc = usc_taxes(gross_salary, ref_row, year_input)
    print("")

    # Call calculate_total_taxes function
    total_taxes = calculate_total_taxes(paye_calc, prsi_calc, usc_calc,
                                        credit_calc, taxable_salary)
    print("")
    print("=================================================================")


main()
