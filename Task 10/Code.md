## 1. Problem Statement
Develop a Python program to calculate hospital bills based on consultation charges, diagnostic charges, and treatment charges. The system applies conditional concessions, validates billing constraints, calculates the final bill, and classifies patients according to their payment amount. It helps hospitals prepare accurate bills and manage patient payment categories.

## 2. Algorithm
1. Start the program.
2. Enter the number of patients.
3. Enter patient name and patient ID.
4. Enter consultation charges, diagnostic charges, and treatment charges.
5. Validate that all charges are non-negative.
6. Calculate the total bill by adding all charges.
7. Apply a 10% concession if the total bill is above ₹10,000.
8. Calculate the final bill after concession.
9. Classify patients according to the payment policy:
   - Below ₹5,000 – Low Payment.
   - ₹5,000 to ₹15,000 – Medium Payment.
   - Above ₹15,000 – High Payment.
10. Display patient details, total bill, concession, final bill, and patient classification.
11. Repeat for all patients.
12. Stop the program.

## 3. Sample Input

Enter number of patients: 2

Enter Patient Details
Enter patient name: Harika
Enter patient ID: P101
Enter consultation charges: 1000
Enter diagnostic charges: 2000
Enter treatment charges: 8000

Enter Patient Details
Enter patient name: Priya
Enter patient ID: P102
Enter consultation charges: 500
Enter diagnostic charges: 1000
Enter treatment charges: 2000

## 4. sampel output

--- Hospital Bill ---

Patient Name: Harika
Patient ID: P101
Consultation Charges: 1000.0
Diagnostic Charges: 2000.0
Treatment Charges: 8000.0
Total Bill: Rs. 11000.0
Concession: Rs. 1100.0
Final Bill: Rs. 9900.0
Patient Category: Medium Payment

--- Hospital Bill ---

Patient Name: Priya
Patient ID: P102
Consultation Charges: 500.0
Diagnostic Charges: 1000.0
Treatment Charges: 2000.0
Total Bill: Rs. 3500.0
Concession: Rs. 0.0
Final Bill: Rs. 3500.0
Patient Category: Low Payment

Hospital Billing Completed.

## 5. Mermaid Flowchart Code

Copy the following code into a Mermaid-compatible editor to generate a flowchart.
 mermaid
 ```mermaid
        
    flowchart TD
    A([Start]) --> B[/Enter Number of Patients/]
    B --> C[/Enter Patient Details/]
    C --> D[/Enter Consultation, Diagnostic and Treatment Charges/]
    D --> E{Charges Valid?}
    E -- No --> F[Display Invalid Charges]
    F --> G{More Patients?}
    E -- Yes --> H[Calculate Total Bill]
    H --> I{Total > 10000?}
    I -- Yes --> J[Apply 10% Concession]
    I -- No --> K[No Concession]
    J --> L[Calculate Final Bill]
    K --> L
    L --> M{Final Bill < 5000?}
    M -- Yes --> N[Low Payment]
    M -- No --> O{Final Bill <= 15000?}
    O -- Yes --> P[Medium Payment]
    O -- No --> Q[High Payment]
    N --> R[Display Hospital Bill]
    P --> R
    Q --> R
    R --> G
    G -- Yes --> C
    G -- No --> S([Stop])
```
### 6. Conclusion
The Hospital Billing and Patient Classification System calculates patient bills accurately using consultation, diagnostic, and treatment charges. It applies concessions, validates charges, and classifies patients according to payment categories. This system reduces manual work and improves hospital billing management.
