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
    if year_input == 2022:
        cell = 2
    elif year_input == 2023:
        cell = 3
    else:
        cell = 4

    # year_row = parameters_worksheet.row_values(x)
    # print(year_row)
    return cell


def tax_credits(marital_status, dependants, cell):
    """
    Calculates the tax credits according to marital status and dependants
    """

    if marital_status == "single":
        if dependants is True:
            credit = (int(parameters_worksheet.cell(cell, 7).value) +
                      int(parameters_worksheet.cell(cell, 9).value) +
                      int(parameters_worksheet.cell(cell, 10).value))
        else:
            credit = (int(parameters_worksheet.cell(cell, 7).value) +
                      int(parameters_worksheet.cell(cell, 10).value))
    elif marital_status == "married":
        credit = (int(parameters_worksheet.cell(cell, 8).value) +
                  int(parameters_worksheet.cell(cell, 10).value))
    else:
        credit = 0
        print("The status input is not valid.")

    print("")
    print(f"Your tax credits are {credit}€")
    return credit, cell


def paye_taxes(taxable_salary, credit, cell):
    """
    Calculates the "Pay As You Earn" taxes applicable to the taxable salary
    """
    paye_year = int(parameters_worksheet.cell(cell, 2).value)

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
    return paye, cell


def prsi_taxes(gross_salary, cell):
    """
    Calculates the PRSI taxes applicable to the gross salary
    """

    prsi_year = int(parameters_worksheet.cell(cell, 3).value)

    if gross_salary < prsi_year:
        prsi = 0
    else:
        prsi = int(gross_salary * 0.04)

    print(f"PRSI = {prsi}€")

    return prsi, cell


def usc_taxes(gross_salary, cell):
    """
    Calculates the Universal Social Charge, applicable to the gross salary
    """

    usc_1_band = int(parameters_worksheet.cell(cell, 4).value)
    usc_2_band = int(parameters_worksheet.cell(cell, 5).value)
    usc_3_band = int(parameters_worksheet.cell(cell, 6).value)

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

    print(f"USC = {usc} € USC")

    return usc, cell


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

    return


def main():
    """
    Runs all program functions
    """
    # parameters_worksheet = SHEET.worksheet('parameters')

    x = 0
    credit = 0
    paye = 0
    prsi = 0
    usc = 0

    print("")
    print("=================================================================")
    print("Welcome to the Irish Tax Income Calculator")
    print("=================================================================")
    print("")

    print("Please select the taxable year:")
    year_input = int(input("Enter 2022 0r 2023\n"))

    print("Please type in your annual gross salary:")
    gross_salary = int(input("Enter your annual gross salary here:\n"))

    print("Are you singularly or jointly assessed?")
    marital_status = input("Enter single or married:\n")

    print("Do you have any dependants?")
    dependants = input("True or False\n")

    print("Do you contribute to any pension scheme?")
    pension = int(input("Enter your annual contributions here:\n"))

    taxable_salary = (gross_salary - pension)

    select_year(year_input)

    cell = select_year(year_input)

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
    credit_calc = tax_credits(marital_status, dependants, cell)
    # paye_taxes(taxable_salary, cell)
    paye_calc = paye_taxes(taxable_salary, credit, cell)
    print("")
    # prsi_taxes(gross_salary, cell)
    prsi_calc = prsi_taxes(gross_salary, cell)
    print("")
    # usc_taxes(gross_salary, cell)
    usc_calc = usc_taxes(gross_salary, cell)
    print("")
    total_taxes = calculate_total_taxes(paye_calc, prsi_calc, usc_calc,
                                        credit_calc, gross_salary)
    # print("")
    print("=================================================================")


main()


# if __name__ == '__main__':
#     main()
