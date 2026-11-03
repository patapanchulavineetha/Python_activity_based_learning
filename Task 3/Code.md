## 1. Problem Statement
Develop a Python program to calculate employee salaries based on basic pay, allowances, overtime, and incentives. The system calculates gross salary, applies progressive deductions according to salary slabs, and determines the final net salary. Finally, it generates a formatted salary statement for each employee.

## 2. Algorithm
1. Start the program.
2. Enter the number of employees.
3. Enter employee name and ID.
4. Enter basic salary, allowances, overtime hours, overtime rate, and incentives.
5. Calculate overtime pay by multiplying overtime hours by overtime rate.
6. Calculate gross salary by adding basic salary, allowances, overtime pay, and incentives.
7. Apply progressive deductions:
   - Gross salary up to ₹20,000: No deduction.
   - ₹20,001 to ₹40,000: 5% deduction.
   - Above ₹40,000: 10% deduction.
8. Calculate the deduction amount.
9. Calculate net salary by subtracting deductions from gross salary.
10. Generate and display the salary statement.
11. Repeat for all employees.
12. Stop the program.

## 3.sample input
input
Enter number of employees: 2

Enter Employee Details
Enter employee name: Harika
Enter employee ID: E101
Enter basic salary: 25000
Enter allowances: 5000
Enter overtime hours: 10
Enter overtime rate: 200
Enter incentives: 2000

Enter Employee Details
Enter employee name: Priya
Enter employee ID: E102
Enter basic salary: 15000
Enter allowances: 3000
Enter overtime hours: 5
Enter overtime rate: 100
Enter incentives: 1000

## 4. sample output

------ SALARY STATEMENT ------

Employee Name: Harika
Employee ID: E101
Basic Salary: Rs. 25000.0
Allowances: Rs. 5000.0
Overtime Pay: Rs. 2000.0
Incentives: Rs. 2000.0
Gross Salary: Rs. 34000.0
Deduction: Rs. 1700.0
Net Salary: Rs. 32300.0

------------------------------

------ SALARY STATEMENT ------

Employee Name: Priya
Employee ID: E102
Basic Salary: Rs. 15000.0
Allowances: Rs. 3000.0
Overtime Pay: Rs. 500.0
Incentives: Rs. 1000.0
Gross Salary: Rs. 19500.0
Deduction: Rs. 0.0
Net Salary: Rs. 19500.0

------------------------------

Payroll Processing Completed.

## 5. Mermaid Flowchart Code

Copy the following code into a Mermaid-compatible editor to generate a flowchart.
 mermaid
 ```mermaid

    flowchart TD
    A([Start]) --> B[/Enter Number of Employees/]
    B --> C[/Enter Employee Details/]
    C --> D[/Enter Basic Pay, Allowances, Overtime and Incentives/]
    D --> E{Are Inputs Valid?}
    E -- No --> F[Display Invalid Details]
    E -- Yes --> G[Calculate Overtime Pay]
    G --> H[Calculate Gross Salary]
    H --> I{Gross <= 20000?}
    I -- Yes --> J[No Deduction]
    I -- No --> K{Gross <= 40000?}
    K -- Yes --> L[Apply 5% Deduction]
    K -- No --> M[Apply 10% Deduction]
    J --> N[Calculate Net Salary]
    L --> N
    M --> N
    N --> O[Generate Salary Statement]
    F --> P{More Employees?}
    O --> P
    P -- Yes --> C
    P -- No --> Q([Stop])
```
## 6.Conclusion
The Employee Payroll and Deduction Analysis System calculates gross salary and net salary using basic pay, allowances, overtime, and incentives. It applies progressive deductions and generates a formatted salary statement. This Python program reduces manual calculations and makes employee payroll processing easier and more accurate.
