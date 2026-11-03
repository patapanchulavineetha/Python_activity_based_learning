## 1.Problem Statement
Develop a Python program to generate a retail bill for multiple products. The system calculates product prices based on quantity, applies category-specific taxes, and provides discounts based on purchase amount. It also applies maximum concession limits to prevent excessive discounts. Finally, the program generates an itemized invoice showing product details, taxes, discounts, and the final payable amount.

## 2. Algorithm
1. Start the program.
2. Enter the number of products.
3. Enter product name, category, price, and quantity.
4. Calculate the subtotal for each product.
5. Apply category-specific taxes:
   - Electronics – 18%.
   - Clothing – 5%.
   - Grocery – 0%.
6. Calculate the total subtotal of all products.
7. Apply threshold discounts:
   - Below ₹1,000 – No discount.
   - ₹1,000 to ₹4,999 – 5% discount.
   - ₹5,000 and above – 10% discount.
8. Apply a maximum discount limit of ₹1,000.
9. Calculate the final bill by adding taxes and subtracting discounts.
10. Display the itemized invoice.
11. Stop the program.

## 3. sample input
Enter number of products: 3

Enter Product Details
Enter product name: Laptop
Enter category (electronics/clothing/grocery): electronics
Enter product price: 30000
Enter quantity: 1

Enter Product Details
Enter product name: Shirt
Enter category (electronics/clothing/grocery): clothing
Enter product price: 1000
Enter quantity: 2

Enter Product Details
Enter product name: Rice
Enter category (electronics/clothing/grocery): grocery
Enter product price: 500
Enter quantity: 2

## 4.sample output

========== RETAIL INVOICE ==========

Product Details:

Product: Laptop
Category: electronics
Price: Rs. 30000.0
Quantity: 1
Amount: Rs. 30000.0
Tax: Rs. 5400.0

Product: Shirt
Category: clothing
Price: Rs. 1000.0
Quantity: 2
Amount: Rs. 2000.0
Tax: Rs. 100.0

Product: Rice
Category: grocery
Price: Rs. 500.0
Quantity: 2
Amount: Rs. 1000.0
Tax: Rs. 0.0

Subtotal: Rs. 33000.0
Total Tax: Rs. 5500.0
Discount: Rs. 1000.0
Final Bill: Rs. 37500.0

Thank You! Visit Again.

## 5. Mermaid Flowchart Code

Copy the following code into a Mermaid-compatible editor to generate a flowchart.
 mermaid
 ```mermaid
       
    flowchart TD
    A([Start]) --> B[/Enter Number of Products/]
    B --> C[/Enter Product Name, Category, Price and Quantity/]
    C --> D{Valid Product Details?}
    D -- No --> E[Display Error]
    D -- Yes --> F[Calculate Product Subtotal]
    F --> G{Select Product Category}
    G -- Electronics --> H[Apply 18% Tax]
    G -- Clothing --> I[Apply 5% Tax]
    G -- Grocery --> J[Apply 0% Tax]
    H --> K[Calculate Total Subtotal and Tax]
    I --> K
    J --> K
    E --> L{More Products?}
    K --> L
    L -- Yes --> C
    L -- No --> M{Subtotal >= 5000?}
    M -- Yes --> N[Apply 10% Discount]
    M -- No --> O{Subtotal >= 1000?}
    O -- Yes --> P[Apply 5% Discount]
    O -- No --> Q[No Discount]
    N --> R[Apply Maximum Discount Limit]
    P --> R
    Q --> R
    R --> S[Calculate Final Bill]
    S --> T[Generate Itemized Invoice]
    T --> U([Stop])
```
## 6. Conclusion
The Retail Billing System calculates product costs, quantities, and category-specific taxes. It applies threshold discounts and maximum concession limits to generate an accurate final bill. This Python program makes retail billing easier, faster, and more organized.
