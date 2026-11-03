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
        rebate =
        
