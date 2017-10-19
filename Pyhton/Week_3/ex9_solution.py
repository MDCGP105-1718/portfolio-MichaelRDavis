# Copyright Chris Janes 2017. All Rights Reserved.
# Author Chris Janes - 19 October 2017

# setup variable declarations
raise_rate = 0.07 # 7%
investment_return = 0.04 # 4%
deposit_percent = 0.25 # 25%
total_cost = 1000000 # £1,000,000
deposit_required = total_cost * deposit_percent

# bisection search variables
low = 0
high = 10000
guess = int((high + low) / 2)
epsilon = 100

steps = 0
rate = guess / 100000

current_search_savings = 0
rate_ok = True

# get some user input for the annual salary amount, we don't do any sanity checks here!
annual_salary = float(input('Enter your annual salary: £'))

# helper function definitions

def get_a_raise(raise_rate, salary):
    """
    raise_rate : decimal percentage of the raise amount (0.07 for 7% etc)
    salary : the current salary amount
    Returns the modified salary value
    """
    salary += salary * raise_rate
    return salary

def calculate_monthly_salary(salary):
    """
    Returns the input salary amount divided by 12
    """
    return salary / 12

def calculate_savings(salary, rate):
    """
    salary: annual salary in decimals (150000 = £150,000)
    rate: monthly savings rate in decimal form (0.05 = 5%)
    Returns the accumulated savings over 36 months
    """
    savings = 0
    monthly_salary = calculate_monthly_salary(salary)
    for month in range(36):
        savings += savings * investment_return / 12
        savings += monthly_salary * (rate)
        if month != 0 and month % 6 == 0:
            salary = get_a_raise(raise_rate, salary)
            monthly_salary = calculate_monthly_salary(salary)

    return savings

# enter the bisection search loop
# keep looping until we have a savings value that is within £100 of the deposit required
while abs(current_search_savings - deposit_required) >= epsilon:
    steps += 1

    # call the calculate_savings to get the 36 months worth of savings with the current guess
    current_search_savings = calculate_savings(annual_salary, rate)

    # if we're below the require deposit, we drop the bottom half of the search space
    # otherwise, we drop the top half
    if  current_search_savings < deposit_required:
        low = guess
    else:
        high = guess

    # this is the break point, if the difference between the high and low values is 1
    # we have failed to find a good savings rate, so we break out and print as much
    if high - low == 1:
        rate_ok = False
        break

    # update the guess value with the new high / low values
    guess = int((high + low)/2)
    # calculate a savings rate from our new guess
    rate = guess / 100000

if rate_ok:
    print("Best savings rate:",str(guess/1000) + "%")
    print("Steps in bisection search:", steps)
else:
    print("It is not possible to pay the down payment in three years")
