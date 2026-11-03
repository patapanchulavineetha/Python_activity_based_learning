## 1. Problem Statement
Develop a Python program to analyze travel expenses in multiple currencies. The system converts expenses into Indian Rupees (INR) using supplied exchange rates and includes currency conversion fees. It calculates the total travel expenditure, compares planned spending with the available budget, and identifies the largest expense category. Finally, it displays the total expenses and budget status.

## 2. Algorithm
1. Start the program.
2. Enter the travel budget in Indian Rupees.
3. Enter the number of expense categories.
4. Enter the following details for each category:
   - Expense category name.
   - Expense amount.
   - Currency type.
   - Exchange rate.
5. Convert the expense amount into Indian Rupees using the exchange rate.
6. Calculate the conversion fee (2% of converted amount).
7. Calculate the total expense including conversion fees.
8. Add all expenses to calculate the total travel cost.
9. Compare total travel cost with the available budget.
10. Identify the largest expense category.
11. Display the expense details, total spending, and remaining budget.
12. Display whether the travel budget is within or above the limit.
13. Stop the program.

## 3. sample input
Enter travel budget in INR: 100000
Enter number of expense categories: 3

Enter Expense Details
Enter expense category: Hotel
Enter expense amount: 300
Enter currency type: USD
Enter exchange rate to INR: 85

Enter Expense Details
Enter expense category: Food
Enter expense amount: 100
Enter currency type: EUR
Enter exchange rate to INR: 90

Enter Expense Details
Enter expense category: Transport
Enter expense amount: 200
Enter currency type: USD
Enter exchange rate to INR: 85

## 4. sample  output
------ TRAVEL EXPENSE REPORT ------

Category: Hotel
Currency: USD
Converted Amount: Rs. 25500.0
Conversion Fee: Rs. 510.0
Total Expense: Rs. 26010.0

Category: Food
Currency: EUR
Converted Amount: Rs. 9000.0
Conversion Fee: Rs. 180.0
Total Expense: Rs. 9180.0

Category: Transport
Currency: USD
Converted Amount: Rs. 17000.0
Conversion Fee: Rs. 340.0
Total Expense: Rs. 17340.0

Total Travel Expense: Rs. 52530.0
Travel Budget: Rs. 100000.0
Remaining Budget: Rs. 47470.0
Status: Within Budget

Largest Expense Category: Hotel

Travel Budget Analysis Completed.

## 5. Mermaid Flowchart Code

Copy the following code into a Mermaid-compatible editor to generate a flowchart.
 mermaid
 ```mermaid

       
    flowchart TD
    A([Start]) --> B[/Enter Travel Budget/]
    B --> C[/Enter Number of Expense Categories/]
    C --> D[/Enter Category, Amount, Currency and Exchange Rate/]
    D --> E{Valid Amount and Rate?}
    E -- No --> F[Display Invalid Details]
    E -- Yes --> G[Convert Amount into INR]
    G --> H[Calculate 2% Conversion Fee]
    H --> I[Calculate Total Expense]
    I --> J[Store Expense Details]
    F --> K{More Categories?}
    J --> K
    K -- Yes --> D
    K -- No --> L[Calculate Total Travel Expense]
    L --> M[Identify Largest Expense Category]
    M --> N{Total Expense <= Budget?}
    N -- Yes --> O[Display Remaining Budget]
    N -- No --> P[Display Budget Exceeded]
    O --> Q[Display Travel Expense Report]
    P --> Q
    Q --> R([Stop])
```
## 6. Conclusion
The Multi-Currency Travel Budget Analysis System converts travel expenses from different currencies into Indian Rupees using exchange rates. It calculates conversion fees, total expenses, and remaining budget. It also identifies the largest expense category and checks whether the travel spending is within the planned budget. This Python program helps travelers manage expenses effectively.
