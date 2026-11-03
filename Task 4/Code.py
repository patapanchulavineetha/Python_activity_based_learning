n = int(input("Enter number of mobile plans: "))


data_needed = float(input("Enter required data (GB): "))
calls_needed = int(input("Enter required call minutes: "))
sms_needed = int(input("Enter required SMS: "))
validity_needed = int(input("Enter required validity (days): "))
budget = float(input("Enter maximum budget: "))

plans = []

for i in range(n):

    print("\nEnter Plan Details")

    name = input("Enter plan name: ")
    price = float(input("Enter plan price: "))
    data = float(input("Enter included data (GB): "))
    calls = int(input("Enter included call minutes: "))
    sms = int(input("Enter included SMS: "))
    validity = int(input("Enter validity days: "))

    if price < 0 or data < 0 or calls < 0 or sms < 0 or validity < 0:
        print("Invalid plan details!")
        continue

    
    extra_data = max(0, data_needed - data)
    extra_calls = max(0, calls_needed - calls)
    extra_sms = max(0, sms_needed - sms)

    
    data_charge = extra_data * 10
    call_charge = extra_calls * 1
    sms_charge = extra_sms * 0.50

    total_cost = price + data_charge + call_charge + sms_charge

    
    if validity >= validity_needed and total_cost <= budget:

        plans.append({
            "name": name,
            "cost": total_cost,
            "data_charge": data_charge,
            "call_charge": call_charge,
            "sms_charge": sms_charge
        })

    print("\nPlan:", name)
    print("Base Price: Rs.", price)
    print("Extra Data Charge: Rs.", data_charge)
    print("Extra Call Charge: Rs.", call_charge)
    print("Extra SMS Charge: Rs.", sms_charge)
    print("Total Cost: Rs.", round(total_cost, 2))


print("\n--- BEST MOBILE PLAN ---")

if len(plans) > 0:

    best = min(plans, key=lambda x: (x["cost"], x["name"].lower()))

    print("Selected Plan:", best["name"])
    print("Total Cost: Rs.", round(best["cost"], 2))
    print("Eligible Plans:", len(plans))

else:
    print("No eligible plans found.")

print("\nProgram Completed.")
