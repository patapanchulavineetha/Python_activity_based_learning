n = int(input("Enter number of products: "))

products = []
subtotal = 0
total_tax = 0

for i in range(n):

    print("\nEnter Product Details")

    name = input("Enter product name: ")
    category = input("Enter category (electronics/clothing/grocery): ").lower()
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    
    if price < 0 or quantity <= 0:
        print("Invalid product details!")
        continue

    
    item_total = price * quantity

    
    if category == "electronics":
        tax_rate = 0.18

    elif category == "clothing":
        tax_rate = 0.05

    elif category == "grocery":
        tax_rate = 0.00

    else:
        print("Invalid category!")
        continue

    tax = item_total * tax_rate

    subtotal += item_total
    total_tax += tax

    products.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "amount": item_total,
        "tax": tax
    })


if subtotal >= 5000:
    discount = subtotal * 0.10

elif subtotal >= 1000:
    discount = subtotal * 0.05

else:
    discount = 0


discount = min(discount, 1000)


final_bill = subtotal + total_tax - discount


print("\n========== RETAIL INVOICE ==========")

print("\nProduct Details:")

for item in products:
    print("\nProduct:", item["name"])
    print("Category:", item["category"])
    print("Price: Rs.", item["price"])
    print("Quantity:", item["quantity"])
    print("Amount: Rs.", round(item["amount"], 2))
    print("Tax: Rs.", round(item["tax"], 2))

print("\nSubtotal: Rs.", round(subtotal, 2))
print("Total Tax: Rs.", round(total_tax, 2))
print("Discount: Rs.", round(discount, 2))
print("Final Bill: Rs.", round(final_bill, 2))

print("\nThank You! Visit Again.")
