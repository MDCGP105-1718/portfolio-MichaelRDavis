total_cost = 0.0 # The total cost of the house
portion_desposit = 0.20 # The portion needed for a deposit
current_savings = 0.0 # The amount saved so far with an additional investment
monthly_salary = (annual_salary/12) # Calculate the monthly salary

annual_salary = float(input("Enter your annual salary: ")) # Enter your annual salary
semi_anual_raise = float(input("Enter your semi annual raise: ")) # Enter your semi-anual raise
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) # Enter the portion you have saved
total_cost = float(input("Enter the cost of your dream home: ")) # Enter the total cost of the house

n = 0
while(current_savings < total_cost * portion_desposit):
    current_savings += current_savings * 0.04/12
    if(n % 6 == 0):
        monthly_salary += semi_anual_raise
    current_savings += monthly_salary * portion_saved
    n += 1

print(f"Number of months: {n}")
