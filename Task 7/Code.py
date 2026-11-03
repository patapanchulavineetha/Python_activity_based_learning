print("MANUFACTURING COST ANALYSIS")


product = input("Enter product name: ")

quantity = int(input("Enter number of units produced: "))

material = float(input("Enter material cost per unit: "))

labour = float(input("Enter labour charges per unit: "))

wastage = float(input("Enter wastage percentage: "))

machine = float(input("Enter total machine cost: "))

selling_price = float(input("Enter selling price per unit: "))

target = float(input("Enter profit target: "))


if (quantity <= 0 or material < 0 or labour < 0
        or wastage < 0 or machine < 0
        or selling_price < 0 or target < 0):

    print("Invalid input details!")

else:

    
    material_cost = material * quantity

    
    wastage_cost = material_cost * wastage / 100

    
    labour_cost = labour * quantity

  
    total_cost = (material_cost + wastage_cost
                  + labour_cost + machine)

    
    revenue = selling_price * quantity

    
    profit = revenue - total_cost

    
    print("\n--- MANUFACTURING REPORT ---")

    print("Product Name:", product)
    print("Quantity Produced:", quantity)

    print("Material Cost: Rs.", material_cost)
    print("Wastage Cost: Rs.", wastage_cost)
    print("Labour Cost: Rs.", labour_cost)
    print("Machine Cost: Rs.", machine)

    print("Total Production Cost: Rs.", round(total_cost, 2))
    print("Total Selling Revenue: Rs.", round(revenue, 2))
    print("Total Profit: Rs.", round(profit, 2))

    print("Profit Target: Rs.", target)

    if profit >= target:
        print("Result: Profit Target Achieved")

    else:
        print("Result: Profit Target Not Achieved")

print("\nProgram Completed.")
