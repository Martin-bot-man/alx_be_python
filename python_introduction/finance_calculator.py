monthly_income= int(input("Enter your monthly income:"));
monthly_expenses = int(input ("Enter your total monthly expenses:"));

monthly_savings = float(monthly_income) - float(monthly_expenses);

annual_interest_rate = 0.05;

Projected_savings = float(monthly_savings) * 12 + float(monthly_savings*12*0.05);

print(f"Your projected savings for the year is: {Projected_savings:.2f}");