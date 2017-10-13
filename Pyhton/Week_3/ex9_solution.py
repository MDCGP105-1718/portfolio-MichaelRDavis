annual_salary = 15000
semi_annual_raise = 0.07
month = 0
monthly_salary = [annual_salary * (1.0 + semi_annual_raise) ** (month) for month in range(36)]
total_cost = 100000 * 0.25
current_savings = total_cost / sum(monthly_salary)

total = 0
for amount in monthly_salary:
    total *= 1.0 + 0.04
    total += amount * current_savings
