## 1. Problem Statement
Develop a Python program to calculate the total expenses required for organizing a campus event. The system calculates venue, equipment, catering, transport, and certificate costs. It determines the total event expenditure, participant contributions, and sponsorship amount. It also identifies the sponsorship shortfall and calculates the minimum number of registrations required to break even. Finally, it displays the complete financial report.

## 2. Algorithm
1. Start the program.
2. Enter the number of expected participants.
3. Enter the following event expenses:
   - Venue cost.
   - Equipment cost.
   - Catering cost per participant.
   - Transport cost per participant.
   - Certificate cost per participant.
4. Enter the sponsorship amount.
5. Enter the registration fee per participant.
6. Calculate total catering, transport, and certificate costs.
7. Calculate total event expenses by adding all costs.
8. Calculate the total sponsorship amount.
9. Calculate the remaining sponsorship shortfall after deducting sponsorship from total expenses.
10. Calculate participant contributions using the registration fee.
11. Calculate the minimum registration count required to break even.
12. Compare expected participants with the break-even count.
13. Display the complete financial report.
14. Stop the program.

## 3. sample input
CAMPUS EVENT FINANCIAL PLANNING

Enter expected participants: 100

Enter venue cost: 20000
Enter equipment cost: 10000

Enter catering cost per participant: 150
Enter transport cost per participant: 50
Enter certificate cost per participant: 20

Enter sponsorship amount: 15000
Enter registration fee per participant: 300

## 4. sample output
------ CAMPUS EVENT FINANCIAL REPORT ------

Expected Participants: 100

--- Event Expenses ---

Venue Cost: Rs. 20000.0
Equipment Cost: Rs. 10000.0
Catering Cost: Rs. 15000.0
Transport Cost: Rs. 5000.0
Certificate Cost: Rs. 2000.0

Total Event Cost: Rs. 52000.0

--- Financial Details ---

Sponsorship: Rs. 15000.0
Participant Contributions: Rs. 30000.0
Registration Fee: Rs. 300.0

Sponsorship Shortfall: Rs. 7000.0

Minimum Registrations for Break-even: 188

Financial Status: Additional Funds Required

Program Completed.

## 5. Mermaid Flowchart Code

Copy the following code into a Mermaid-compatible editor to generate a flowchart.
 mermaid
 ```mermaid
       
    flowchart TD
    A([Start]) --> B[/Enter Expected Participants/]
    B --> C[/Enter Venue and Equipment Costs/]
    C --> D[/Enter Catering, Transport and Certificate Costs/]
    D --> E[/Enter Sponsorship and Registration Fee/]
    E --> F{Are Inputs Valid?}
    F -- No --> G[Display Invalid Input]
    F -- Yes --> H[Calculate Fixed Costs]
    H --> I[Calculate Varia
    ble Costs]
    I --> J[Calculate Total Event Expenses]
    J --> K[Calculate Participant Contributions]
    K --> L[Calculate Funding Shortfall]
    L --> M[Calculate Break-even Registrations]
    M --> N{Shortfall = 0?}
    N -- Yes --> O[Budget Covered]
    N -- No --> P[Additional Funds Required]
    O --> Q[Display Financial Report]
    P --> Q
    G --> R([Stop])
    Q --> R
```
## 10. Conclusion
The Campus Event Financial Planning System calculates all expenses required for organizing a college event. It determines participant contributions, sponsorship shortfalls, and the minimum number of registrations needed to break even. This Python program helps colleges manage event budgets, control expenses, and plan financial resources effectively.
