# Asking user to write their monthly incomes along with expenses
income = float(input("Enter a monthly income"))
transport = float(input("Enter your monthly transport expenses:"))
home_rent = float(input("Enter your monthly rent:"))
food_groceries = float(input("Enter your monthly food and groceries expenses:"))
electricity = float(input("Enter electicity bill:"))
emergency = float(input("Enter your monthly emergency expenses:"))

# Showing money before expenses
print("Money before expenses:", income)

# Calculating the total amount 
total_expenses = transport + food_groceries + home_rent + electricity +  emergency

# Remaining balance 
balance = income - total_expenses
print("Your remaining balance is:", balance)


