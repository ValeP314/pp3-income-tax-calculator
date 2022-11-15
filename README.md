
## Reminders

* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.




# The Tax Income Calculator

The purpose of this project is to build a front-end site. The site should respond to the users' actions, allowing users to actively engage with data, alter the way the site displays the information to achieve their preferred goals. 


I decided to create an interactive app, that allows you to be in charge of your salary and taxes. It is possible to select the tax year (between 2022 and 2023) and check the individual deductions, the total deductions and the net pay. 
The net pay is also manipulated in order to get an annual earning value along with more immediate (and possibly meaningful) monthly and weekly values.
This app is developed using Python.

## Project Inspiration
The idea comes from the need of understanding better my payslip, especially since the new 2023 Budget has been released.

![MockUp](./assets/images/...)


## Flowchart
The following flowchart supported me in designing the final output of the application, as help me in keeping track of al the parameters I needed to factor in:

![Flowchart](./assets/images/...)

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
    

## Testing 

- I tested this page in different browsers: Chrome, Edge, Safari.
- The project is responsive, and it looks and works well on different browsers and screen sizes.


### Validator Testing 

- Python
  - 


### Fixed Bugs
- Some calculations were longer than the 79 characters allowed in PEP8, so I researched on best practices  


### Unfixed Bugs
None

## Deployment

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab.
  - From the menu, select Pages.
  - From the Branch section drop-down menu, select the Main Branch.
  - Once the main branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

  The live link can be found here - [The Daisy Game](https://valep314.github.io/pp2-daisy/)


## Credits  

### Content 

- The main structure is inspired to the Love Sandwiches project.
- The README file uses the structure of my previous project [The Daisy Game](https://github.com/ValeP314/pp2-daisy/blob/main/README.md)
- Inspiration on the main contents of this project came from this video from [Girl Coder](https://www.usandopy.com/en/tutorial/exercise-1-build-a-salary-calculator-in-python/).
- [Stackoverflow](https://stackoverflow.com/) was consulted regularly for tips on general coding. 
- All tax bands are actual and updated, and were taken from [Revenue](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx) or [Citizen Information](https://www.citizensinformation.ie/en/money_and_tax/budgets/budget_2023.html).


### Acknowledgment




### Disclaimer

The information provided on this site is intended for educational purposes only.