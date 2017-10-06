#The total cost of the house
total_cost = 0.0
#The portion needed for a deposit
portion_desposit = 0.20
#The amount saved so far with an additional investment
current_savings = 0.0
#Enter your annual salary
annual_salary = float(input("Enter you annual salary: "))
#Enter the portion you have saved
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
#Enter the total cost of the house
total_cost = float(input("Enter the cost of your dream home: "))
#Calculate the monthly salary
monthly_salary = (annual_salary/12)
n = 0
while(current_savings < total_cost * portion_desposit):
    current_savings += current_savings * 0.04/12
    current_savings += monthly_salary * portion_saved
    n += 1

print(f"Number of months: {n}")
