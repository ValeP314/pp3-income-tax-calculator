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

# print("What is your name?")
# full_name = input("Enter your full name here:\n")

print("Please select the taxable year:")
year = int(input("Enter the relevant tax year\n"))

print("Please type in your annual gross salary:")
gross_salary = int(input("Enter your annual gross salary here:\n"))

print("Are you singularly or jointly assessed?")
marital_status = input("Enter single or married:\n")

print("Do you have any dependants?")
dependants = input("True or False\n")

print("Do you contribute to any pension scheme?")
pension = int(input("Enter your annual contributions here:\n"))

taxable_salary = (gross_salary - pension)
print(f"Your taxable salary is {taxable_salary} €")

credit = 0
paye = 0
prsi = 0
usc = 0


def select_year():
    global x

    if year == 2022:
        x = 2
    elif year == 2023:
        x = 3
    else:
        x = 4

    # year_row = parameters_worksheet.row_values(x)
    # print(year_row)
    return x


def tax_credits():
    """
    Calculates the tax credits according to marital status and dependants
    """
    global credit
    select_year()

    if marital_status == "single" and dependants is True:
        credit = (int(parameters_worksheet.cell(x, 7).value) + 
                  int(parameters_worksheet.cell(x, 9).value) + 
                  int(parameters_worksheet.cell(x, 10).value))
    elif marital_status == "single" and dependants is not True:
        credit = (int(parameters_worksheet.cell(x, 7).value) + 
                  int(parameters_worksheet.cell(x, 10).value))
    elif marital_status == "married":
        credit = (int(parameters_worksheet.cell(x, 8).value) + 
                  int(parameters_worksheet.cell(x, 10).value))
    else:
        print("The input is not a valid status")
    print(f"Your tax credits are {credit}")


def paye_taxes():
    """
    Calculates the "Pay As You Earn" taxes applicable to the taxable salary
    """
    global paye

    select_year()

    paye_year = int(parameters_worksheet.cell(x, 2).value)

    if taxable_salary < paye_year:
        paye = taxable_salary * 0.20
    else:
        excess_paye = taxable_salary - paye_year
        first_band_paye_taxes = paye_year * 0.20
        paye = (first_band_paye_taxes + (excess_paye * 0.40))

    print(f"You pay {paye} € PAYE")
    print(f"{paye_year}")
    return paye


def prsi_taxes():
    """
    Calculates the PRSI taxes applicable to the gross salary
    """
    global prsi

    select_year()

    prsi_year = int(parameters_worksheet.cell(x, 3).value)

    if gross_salary < prsi_year:
        prsi = 0
    else:
        prsi = int(gross_salary * 0.04)

    print(f"You pay {prsi} € PRSI")
    print(f"{prsi_year}")
    return prsi


def usc_taxes():
    """
    Calculates the Universal Social Charge, applicable to the gross salary
    """
    global usc

    select_year()

    usc_1_band = int(parameters_worksheet.cell(x, 4).value)
    usc_2_band = int(parameters_worksheet.cell(x, 5).value)
    usc_3_band = int(parameters_worksheet.cell(x, 6).value)

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

    print(f"You pay {usc} € USC")
    print(f"{usc_1_band}")
    print(f"{usc_2_band}")
    print(f"{usc_3_band}")
    return usc


def calculate_total_taxes():
    """
    Adds the 3 contributions in order to calculate annual net pay
    """
    total_taxes = int(paye) + int(prsi) + int(usc)
    print(f"You pay a total of {total_taxes} € in taxes")
    net_pay = gross_salary - total_taxes
    print(f"Your annual net pay is {net_pay} €")


def main():
    """
    Runs all program functions
    """
    tax_credits()
    paye_taxes()
    prsi_taxes()
    usc_taxes()
    calculate_total_taxes()


main()
