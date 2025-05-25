monthly_income= int(input("Enter your monthly income : "));
monthly_expense = int(input ("Enter your monthly expense : "));

monthly_savings = monthly_income - monthly_expense;

annual_interest_rate = 0.05;

Projected_savings = monthly_savings * 12 + (monthly_savings*12*0.05);

print(f"Your projected savings for the year is: {Projected_savings:.2f}");