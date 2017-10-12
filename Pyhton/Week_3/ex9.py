# Your semi-anual raise (every 6 months)
semi_annual_raise = 0.07

# Your annual rate of return for your investments
annaul_rate = 0.04

# The down payment needed for the house
down_payment = 0.25

# The total cost of your house
total_cost = 1000000

# Your current savings
current_savings = 0.0

# The number of months to achieve your down payment for the house
months = 0

# The number of bisection steps
bisection_steps = 0

# Low value
low = 0

# High value
high = 10000

# The percentage amount currently saved
percent_saved = int((low + high) / 2)

# Enter your starting salary
starting_salary = float(input("Enter the starting salary: "))

# Calculate the monthly salary
monthly_salary = (starting_salary / 12)

# While months is less than 36 calculate the best saving rate for a house down payment
while(months <= 36):
    percent_saved = percent_saved / 10000
    monthly_salary += monthly_salary * semi_annual_raise
    current_savings += current_savings * annaul_rate / 12
    current_savings += monthly_salary * percent_saved

    # If current savings is less than the down payment needed for the house
    if(current_savings < down_payment):
        low = percent_saved
    # If current savings is greater than the down payment needed for the house
    elif(current_savings > down_payment):
        high = percent_saved
    else:
        print("It is not possible to pay the down payment in three years")

    percent_saved = ((low + high) / 2)

    # Print the best savings rate
    print(f"Best savings rate: {percent_saved}\n")

    # Print number of steps in bisection search
    print(f"Steps in bisection search: {bisection_steps}\n")

    months += 1
    bisection_steps += 1
