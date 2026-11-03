## 1. Problem Statement
Develop a Python program to calculate manufacturing costs and analyze product profitability. The system calculates material costs, labour charges, wastage costs, and machine costs. It determines the total production cost, selling price, and profit earned. Finally, it compares the actual profit with a specified profit target and identifies whether the production meets the target.

## 2. Algorithm
1. Start the program.
2. Enter the product name and number of units produced.
3. Enter material cost per unit.
4. Enter labour charges per unit.
5. Enter wastage percentage.
6. Enter machine cost.
7. Enter selling price per unit.
8. Enter the required profit target.
9. Calculate total material cost.
10. Calculate wastage cost based on material cost.
11. Calculate total labour cost.
12. Calculate total production cost by adding material, wastage, labour, and machine costs.
13. Calculate total selling revenue.
14. Calculate profit by subtracting production cost from selling revenue.
15. Compare actual profit with the target profit.
16. Display whether the production meets the profit target.
17. Stop the program.

## sample input

MANUFACTURING COST ANALYSIS

Enter product name: Chairs
Enter number of units produced: 100
Enter material cost per unit: 200
Enter labour charges per unit: 50
Enter wastage percentage: 10
Enter total machine cost: 2000
Enter selling price per unit: 350
Enter profit target: 5000

## sample output

--- MANUFACTURING REPORT ---

Product Name: Chairs
Quantity Produced: 100

Material Cost: Rs. 20000.0
Wastage Cost: Rs. 2000.0
Labour Cost: Rs. 5000.0
Machine Cost: Rs. 2000.0

Total Production Cost: Rs. 29000.0
Total Selling Revenue: Rs. 35000.0
Total Profit: Rs. 6000.0

Profit Target: Rs. 5000.0

Result: Profit Target Achieved

Program Completed.

## 5. Mermaid Flowchart Code

Copy the following code into a Mermaid-compatible editor to generate a flowchart.
 mermaid
 ```mermaid
        

    flowchart TD
    A([Start]) --> B[/Enter Product Details/]
    B --> C[/Enter Material, Labour and Wastage Costs/]
    C --> D[/Enter Machine Cost and Selling Price/]
    D --> E[/Enter Profit Target/]
    E --> F{Are Inputs Valid?}
    F -- No --> G[Display Invalid Input]
    F -- Yes --> H[Calculate Material Cost]
    H --> I[Calculate Wastage Cost]
    I --> J[Calculate Labour Cost]
    J --> K[Calculate Total Production Cost]
    K --> L[Calculate Selling Revenue]
    L --> M[Calculate Total Profit]
    M --> N{Profit >= Target?}
    N -- Yes --> O[Profit Target Achieved]
    N -- No --> P[Profit Target Not Achieved]
    O --> Q[Display Manufacturing Report]
    P --> Q
    G --> R([Stop])
    Q --> R
```
## 6. Conclusion
The Manufacturing Cost and Profitability Analysis System calculates material costs, labour charges, wastage, and machine costs. It determines the total production cost and selling profit. It also checks whether the actual profit meets the specified target. This Python program helps manufacturers understand production expenses and make better business decisions.
