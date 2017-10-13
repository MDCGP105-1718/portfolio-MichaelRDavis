semi_annual_raise = 0.07 # Your semi-anual raise (every 6 months)
annaul_rate = 0.04 # Your annual rate of return for your investments
total_cost = 1000000 # The total cost of your house
down_payment = 0.25 * total_cost # The down payment needed for the house
current_savings = 0.0 # Your current savings
months = 0 # The number of months to achieve your down payment for the house
bisection_steps = 0 # The number of bisection steps
low = 0 # Low value
high = 10000 # High value
epsilon = 100 # Epsilon

percent_saved = int((low + high) / 2) # The percentage amount currently saved
starting_salary = float(input("Enter the starting salary: ")) # Enter your starting salary
monthly_salary = (starting_salary / 12) # Calculate the monthly salary

# While months is less than 36 calculate the best saving rate for a house down payment
while(current_savings - down_payment >= epsilon and months <= 36):
    current_savings += monthly_salary * percent_saved
    current_savings += current_savings * annaul_rate / 12
    if(months % 6 == 0):
        monthly_salary += monthly_salary * semi_annual_raise
    while True:
        # If current savings is less than the down payment needed for the house look lower
        if(current_savings < down_payment):
            low = percent_saved
            # If current savings is greater than the down payment needed for the house look higher
        elif(current_savings > down_payment):
            high = percent_saved
        else:
            print("It is not possible to pay the down payment in three years")

            percent_saved = ((low + high) / 2)

            bisection_steps += 1
            months += 1

print(f"Best savings rate: {percent_saved}\n") # Print the best savings rate
print(f"Steps in bisection search: {bisection_steps}\n") # Print number of steps in bisection search
