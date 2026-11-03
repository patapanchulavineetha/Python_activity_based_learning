months = int(input("Enter number of months: "))

bills = []

for i in range(months):

    print("\nMonth", i + 1)

    month = input("Enter month name: ")
    units = float(input("Enter electricity units: "))

    
    if units <= 100:
        energy = units * 2

    elif units <= 200:
        energy = (100 * 2) + (units - 100) * 3

    else:
        energy = (100 * 2) + (100 * 3) + (units - 200) * 5

    fixed = 50
    surcharge = energy * 0.05

    
    if units < 100:
        rebate = energy * 0.05
    else:
        rebate = 0

    total = energy + fixed + surcharge - rebate

    bills.append({
        "month": month,
        "units": units,
        "bill": total
    })


print("\n--- Monthly Electricity Bills ---")

for item in bills:
    print(item["month"], "- Units:", item["units"],
          "- Bill: Rs.", round(item["bill"], 2))


print("\n--- Unusual Bill Increases ---")

found = False

for i in range(1, len(bills)):

    previous = bills[i - 1]["bill"]
    current = bills[i]["bill"]

    if previous > 0:
        increase = ((current - previous) / previous) * 100

        if increase > 30:
            print("Unusual increase in", bills[i]["month"])
            print("Increase:", round(increase, 2), "%")
            found = True

if not found:
    print("No unusual increases found.")

print("\nTotal Months:", months)
print("Program Completed.")
