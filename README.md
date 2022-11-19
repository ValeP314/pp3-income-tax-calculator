# The Tax Income Calculator

The purpose of this project is to build a web application using Python. The site should respond to the users' actions, allowing users to actively engage with data, alter the way the site displays the information to achieve their preferred goals. 


I decided to create an interactive application, that allows you to be in charge of your salary and taxes. It is possible to select the tax year (between 2022 and 2023) and check the individual deductions, the total deductions and the net pay. 
The net pay is also manipulated in order to get an annual earning value along with more immediate (and possibly meaningful) monthly and weekly values.
This app is developed using Python and is deployed in Heroku.

## Project Inspiration
The idea comes from the need of understanding better my payslip, especially since the new 2023 Budget has been released.


## Features

### Existing Features

- __Introduction area__
    The first part of the program asks for specific questions, such as gross salary, tax year, marital status and potential pension contribution.

- __Calculation area__
    The program will then calculate and return the individual values for tax credits, PAYE, USC, PRSI. 
    The sum af this will give the total amount of taxes paid annually.
    The system will also calculate the net pay, by year, month or week.


### Features Left to Implement

- The Google sheet will be easy to implement whenever the 2024 Budget will become available. This can be done by appending a row to the information already present in the worksheet, or directly adding the new band values onto the worksheet itself.
- In order to provide a better experience, it would be beneficial to implement some HTML and CSS features to create a user-friendly interface.
    

## Testing 

- I tested this page in different browsers: Chrome, Edge, Safari.
- The project is responsive, and it looks and works well on different browsers and screen sizes.


### Validator Testing 

- CI Python Linter:
  - The CI Python Linter returned no errors.


### Fixed Bugs
- Some calculations were longer than the 79 characters allowed in PEP8, so I researched on best practices and learned how to break the lines in the correct way.


### Unfixed Bugs
None

## Deployment

- The site was deployed to Heroku. The steps to deploy are as follows: 
  - In the dashboard, create a new app and name it with a unique name.
  - Select the region (Europe) and press Create.
  - In the Settings tab, create a Config Var called CREDS and paste the JSON into the value field, to store sensitive data.
  - Create a new Config Var called PORT and add 8000 in the value field.
  - Add two buildpacks from the Settings tab. They must be ordered as follows:
    1. heroku/python
    2. heroku/nodejs
  - In the Deploy tab, select Github as deploy method and connect it to Github.
  - Search for the relevant repository and then clck connect.
  - Set up automatic or manual deployment.
  - Wait while the app is being build, and all packages are being installed. 
  - Finally, the “App was  successfully deployed” message will show on screen, together with a button to take us to our deployed  link. 

  The live link can be found here - [The Tax Income Calculator](https://tax-income-calculator.herokuapp.com/)


## Credits  

### Content 

- The main structure is inspired to the Love Sandwiches project.
- The README file uses the structure of my previous project [The Daisy Game](https://github.com/ValeP314/pp2-daisy/blob/main/README.md)
- Inspiration on the main contents of this project came from this video from [Girl Coder](https://www.usandopy.com/en/tutorial/exercise-1-build-a-salary-calculator-in-python/).
- [Stackoverflow](https://stackoverflow.com/) was consulted regularly for tips on general coding. 
- All tax bands are actual and updated, and were taken from [Revenue](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx) or [Citizen Information](https://www.citizensinformation.ie/en/money_and_tax/budgets/budget_2023.html).


### Disclaimer

The information provided on this site is intended for educational purposes only.