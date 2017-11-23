total_cost = 0.0 # The total cost of the house
portion_desposit = 0.20 # The portion needed for a deposit
current_savings = 0.0 # The amount saved so far with an additional investment
annual_salary = 0
monthly_salary = (annual_salary / 12) # Calculate the monthly salary

while True:
    try:
        annual_salary = float(input("Enter you annual salary: ")) # Enter your annual salary
        portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) # Enter the portion you have saved
        total_cost = float(input("Enter the cost of your dream home: ")) # Enter the total cost of the house
        break
    except ValueError:
        continue

# Calculate How many months it would take to make a down paymnet for a house?
n = 0
while(current_savings < total_cost * portion_desposit):
    current_savings += current_savings * 0.04/12
    current_savings += monthly_salary * portion_saved
    n += 1

print(f"Number of months: {n}")
