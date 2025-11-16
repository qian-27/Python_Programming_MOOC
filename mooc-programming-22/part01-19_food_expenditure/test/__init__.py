# Write your solution here
eat_at_cafeteria = float(input("How many times a week do you eat at the student cafeteria?"))
price_of_lunch = float(input("The price of a typical student lunch?"))
grocery_money = float(input("How much money do you spend on groceries in a week?"))
 
weekly_expense = eat_at_cafeteria * price_of_lunch + grocery_money
daily_expense = round(weekly_expense / 7, 2)
 
print(f"\nAverage food expenditure:")
print(f"Daily: {daily_expense} euros")
print(f"Weekly: {weekly_expense} euros")