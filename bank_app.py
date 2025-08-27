def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

income = get_positive_float("Enter your monthly income: ")
transport = get_positive_float("Enter your monthly transport expenses: ")
home_rent = get_positive_float("Enter your monthly rent: ")
food_groceries = get_positive_float("Enter your monthly food and groceries expenses: ")
electricity = get_positive_float("Enter electricity bill: ")
emergency = get_positive_float("Enter your monthly emergency expenses: ")

# Optional: Savings
save_percent = get_positive_float("Enter percentage of income to save (0 if none): ")
savings = income * (save_percent / 100)

# Calculating the total amount 
total_expenses = transport + food_groceries + home_rent + electricity + emergency + savings

# Remaining balance 
balance = income - total_expenses

# Summary
print("\n--- Monthly Summary ---")
print(f"Income:           {income:.2f}")
print(f"Transport:        {transport:.2f}")
print(f"Home Rent:        {home_rent:.2f}")
print(f"Food & Groceries: {food_groceries:.2f}")
print(f"Electricity:      {electricity:.2f}")
print(f"Emergency:        {emergency:.2f}")
print(f"Savings:          {savings:.2f}")
print(f"Total Expenses:   {total_expenses:.2f}")
print(f"Remaining Balance:{balance:.2f}")
