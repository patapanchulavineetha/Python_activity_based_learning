budget = float(input("Enter travel budget in INR: "))

n = int(input("Enter number of expense categories: "))

expenses = []
total_expense = 0

for i in range(n):

    print("\nEnter Expense Details")

    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency type: ").upper()
    rate = float(input("Enter exchange rate to INR: "))

    
    if amount < 0 or rate <= 0:
        print("Invalid expense details!")
        continue

    
    converted = amount * rate


    fee = converted * 0.02

    
    total = converted + fee

    total_expense += total

    expenses.append({
        "category": category,
        "currency": currency,
        "converted": converted,
        "fee": fee,
        "total": total
    })


if len(expenses) > 0:

    largest = max(expenses, key=lambda x: x["total"])

  
    print("\n------ TRAVEL EXPENSE REPORT ------")

    for item in expenses:

        print("\nCategory:", item["category"])
        print("Currency:", item["currency"])
        print("Converted Amount: Rs.", round(item["converted"], 2))
        print("Conversion Fee: Rs.", round(item["fee"], 2))
        print("Total Expense: Rs.", round(item["total"], 2))

    print("\nTotal Travel Expense: Rs.", round(total_expense, 2))
    print("Travel Budget: Rs.", budget)

    remaining = budget - total_expense

    if remaining >= 0:
        print("Remaining Budget: Rs.", round(remaining, 2))
        print("Status: Within Budget")

    else:
        print("Budget Exceeded: Rs.", round(abs(remaining), 2))
        print("Status: Over Budget")

    print("Largest Expense Category:", largest["category"])

else:
    print("No valid expenses entered.")

print("\nTravel Budget Analysis Completed.")
