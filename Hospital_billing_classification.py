

1. COMPUTATIONAL THINKING (Compulsory)
- *Decomposition:* Patient Input -> Consultation + Diagnostic + Treatment Charges -> Concession Calculation (fractions) -> Billing Constraints Validation -> Patient Classification per Payment Policy -> Summary
- *Pattern Recognition:* `subtotal = consult + diag + treat` , `concession = subtotal * fraction` repeats
- *Abstraction:* Patient as nested list `[ID,Name,Age,Type,Dept,BPL,Insurance,Days,Consult,Diag,Treat]`
- *Algorithm:* Fraction based concession policy

2. ALGORITHM (Compulsory)
START
 INIT dept_rates tuple (("General",500),...) and concession_policy tuple with fractions (0.15,0.10,0.20,0.25)
 INIT patients=[] bills=[] nested lists
 WHILE menu:
  1 Input: id STR, name STR, age INT, dept STR, bpl STR, insurance STR, days INT
    VALIDATE: age 0-120, days>=0, id not duplicate, type Inpatient/Outpatient
  2 Calculate: input consult INT, diag INT, treat INT
    VALIDATE: consult>=0, diag>=0, treat>=0, consult<=50000, diag<=100000, treat<=200000 (billing constraints)
    sub = consult + diag + treat
    conc = 0
    IF age>60: conc += sub * 15/100 (fraction 0.15)
    ELIF age<12: conc += sub * 10/100 (fraction 0.10)
    IF bpl=="Yes": conc += sub * 20/100 (fraction 0.20)
    IF insurance=="Yes": conc += sub * 25/100 (fraction 0.25)
    IF conc > sub*50/100: conc = sub*0.5 (cap validation)
    total = sub - conc
    VALIDATE total>0
    CLASSIFY: IF total>50000 High ELIF >20000 Medium ELSE Low per payment policy
  3 View bills with unpacking
  4 Classify with payment_status
  5 Summary pattern ### chart + dept wise
  6 Exit pattern
END
3. PSEUDOCODE (Compulsory)
SET dept_rates = (("General",500),("Cardio",1000),...)
SET concession_policy = (("Senior",60,15/100),("Child",12,10/100),("BPL",20/100),("Insurance",25/100))
SET patients=[], bills=[]
WHILE True:
 DISPLAY Menu
 READ choice
 IF choice==1:
  READ pid STRING, name STRING, age INT, dept STRING, bpl STRING, insurance STRING, days INT
  IF age<0 or age>120: PRINT invalid
  ELSE APPEND [pid,name,age,dept,bpl,insurance,days,0,0,0]
 IF choice==2:
  FOR each patient: READ consult,diag,treat
  sub=consult+diag+treat
  conc = sub*0.15 IF age>60 ELSE sub*0.10 IF age<12
  IF bpl=="Yes": conc+=sub*0.20 // fraction
  total=sub-conc
  IF total>50000 cat="High"
  APPEND to bills
4. FLOWCHART - COPYABLE TEXT - FOR RECORD
==================== HOSPITAL BILLING FLOWCHART - COPYABLE ====================

[START - Oval]
   |
   V
[Rectangle - PROCESS] Initialize:
   dept_rates = (("General",500),("Cardio",1000),("Ortho",800),("Neuro",1200),("Pedia",400)) // Tuple
   concession_policy = (("Senior",60,0.15),("Child",12,0.10),("BPL",0,0.20),("Insurance",0,0.25)) // Tuple with fractions
   patients = [] // List - Nested List
   bills = [] // List - Nested List
   |
   V
[Parallelogram - I/O] DISPLAY MENU:
   1 Add Patient
   2 Calculate Bill (Consultation+Diagnostic+Treatment)
   3 View Bills
   4 Classify Patients per Payment Policy
   5 Summary Report
   6 Exit
   |
   V
[Diamond - DECISION] Input choice?

PATH 1 - Add Patient:
  [Rectangle] Input pid STRING, name STRING, age INT, ptype STRING, dept STRING, bpl STRING, insurance STRING, days INT // Variables, Data Types, Strings
  [Diamond] Validate age>=0 and age<=120 and days>=0? // Operators, Conditional
    No -> [Rectangle] Print "Invalid" -> Back to Menu
    Yes -> [Rectangle] patients.append([pid,name,age,ptype,dept,bpl,insurance,days,0,0,0]) // Nested List -> Back to Menu

PATH 2 - Calculate Bill:
  [Rectangle] Loop: For p in patients: // Loops
  [Rectangle] Unpack: pid,name,age,ptype,dept,bpl,insurance,days,c1,c2,c3 = p // Unpacking 11 values
  [Rectangle] Input consult INT, diag INT, treat INT // Variables, Data Types
  [Diamond] Validate billing constraints: consult>=0 and diag>=0 and treat>=0 and consult<=50000? // Operators + Validation
    No -> Back
    Yes -> [Rectangle] subtotal = consult + diag + treat // Operator +
  [Diamond] age>60? // Conditional
    Yes -> [Rectangle] Loop concession_policy tuple: for policy,threshold,percent in concession_policy: // Tuple operations + Unpacking 3
              if policy=="Senior": concession += subtotal*percent // Fraction 15/100
    No -> [Diamond] age<12?
           Yes -> concession += subtotal*10/100 // Fraction
  [Diamond] bpl.lower()=="yes"? // String operation lower(), Conditional
    Yes -> concession += subtotal*20/100 // Fraction
  [Diamond] insurance.lower()=="yes"?
    Yes -> concession += subtotal*25/100 // Fraction
  [Diamond] concession > subtotal*50/100? // Validation cap
    Yes -> [Rectangle] concession = subtotal*50/100
  [Rectangle] total = subtotal - concession // Operator -
  [Diamond] total>0? // Billing constraint validation
    No -> Error
    Yes -> [Rectangle] Classify:
            IF total>50000: category="High" // Conditional
            ELIF total>20000: category="Medium"
            ELSE: category="Low"
            IF concession>0: payment="Concession" ELSE "Paid"
            IF insurance: payment+="-Insurance Pending" // String +
  [Rectangle] bills.append([pid,name,age,subtotal,concession,total,category,payment,dept,bpl]) // Nested List
  -> Back to Menu

PATH 3 - View Bills:
  [Rectangle] Loop bills: for b in bills: // Loops
  [Rectangle] Unpack: pid,name,age,sub,conc,total,cat,pay,dept,bpl = b // Unpacking 10
  [Parallelogram] Display
  -> Back

PATH 4 - Classify:
  [Rectangle] Payment Policy: High>50000, Medium>20000, Low<=20000 per policy
  [Parallelogram] Display classification
  -> Back

PATH 5 - Summary:
  [Rectangle] Count low,med,high using loops // Variables, Loops
  [Rectangle] Pattern Generation: For label,count in [("Low",low),...]: // List + Tuple
                bar = "#" * count // Pattern generation ###
                Print bar
  [Rectangle] Dept-wise total using nested list loops
  -> Back

PATH 6 - Exit:
  [Rectangle] Pattern Generation:
            For i in range(5,0,-1): print("*"*i + " THANK YOU " + "*"*i) // Pattern
  [Oval - END]

5. COMPLETE PYTHON CODE - ONLY SYLLABUS ALLOWED
03_hospital_billing_classification.py
Syllabus ONLY: computational thinking, algorithms, flowcharts, pseudocode, variables, data types, operators, conditionals, loops, strings, pattern, lists, nested lists, tuples, tuple ops, unpacking

TUPLES with fractions - payment policy
dept_rates = (("General",500),("Cardiology",1000),("Ortho",800),("Neurology",1200),("Pediatrics",400))
Concession policy tuple with fractions: Senior 15/100=0.15, Child 10/100=0.10, BPL 20/100=0.20, Insurance 25/100=0.25
concession_policy = (("Senior",60,15/100),("Child",12,10/100),("BPL",0,20/100),("Insurance",0,25/100))

NESTED LISTS
patients = []  # each patient = [id,name,age,type,dept,bpl,insurance,days,consult,diag,treat]
bills = []     # each bill = [id,name,age,subtotal,concession,total,category,payment_status,dept,bpl]

def calculate_concession(age, bpl, insurance, subtotal):
    # VARIABLES - float, int
    concession = 0.0  # float data type
    # CONDITIONAL STATEMENTS + TUPLE OPERATIONS + UNPACKING + OPERATORS + FRACTIONS
    if age > 60:  # senior
        for policy, threshold, percent in concession_policy:  # loop + tuple unpacking 3 values
            if policy == "Senior":  # string + conditional
                concession += subtotal * percent  # fraction 15/100
                break
    elif age < 12:  # child
        for policy, threshold, percent in concession_policy:
            if policy == "Child":
                concession += subtotal * percent  # fraction 10/100
                break
    # STRING operations lower()
    if bpl.lower() == "yes":
        for policy, threshold, percent in concession_policy:
            if policy == "BPL":
                concession += subtotal * percent  # fraction 20/100
                break
    if insurance.lower() == "yes":
        for policy, threshold, percent in concession_policy:
            if policy == "Insurance":
                concession += subtotal * percent  # fraction 25/100
                break
    # VALIDATION - billing constraints - concession cap 50%
    if concession > subtotal * 50/100:  # fraction 50/100
        concession = subtotal * 50/100
    return concession

def classify_patient(total, concession, insurance):
    # CONDITIONAL STATEMENTS
    if total > 50000:
        category = "High"
    elif total > 20000:
        category = "Medium"
    else:
        category = "Low"
    if concession > 0:
        payment_status = "Concession"
    else:
        payment_status = "Paid"
    if insurance.lower() == "yes":
        payment_status = payment_status + "-Insurance Pending"  # string operator +
    return category, payment_status

def show_pattern(title):
    # PATTERN GENERATION + LOOPS + STRINGS
    print("\n" + "="*60)
    for i in range(1,4):  # loop + range
        print("*" * i + " " + title + " " + "*" * i)  # pattern * + string
    print("="*60)

MAIN MENU - LOOPS
while True:  # loop while
    show_pattern("HOSPITAL BILLING")
    print("1.Add Patient\n2.Calculate Bill\n3.View Bills\n4.Classify\n5.Summary\n6.Exit")
    ch = input("Choice: ").strip()  # string strip()

    if ch == "1":  # conditional
        show_pattern("Add Patient")
        pid = input("Patient ID: ").strip().upper()  # string upper()
        exists = False
        for p in patients:  # loop + list
            if p[0] == pid:  # nested list indexing
                exists = True
                break
        if exists:
            print("ID exists!")
        else:
            name = input("Name: ").strip().title()  # string title()
            try:
                age = int(input("Age: ").strip())  # int data type
                ptype = input("Type Inpatient/Outpatient: ").strip().title()
                dept = input("Dept: ").strip().title()
                bpl = input("BPL Yes/No: ").strip().title()
                insurance = input("Insurance Yes/No: ").strip().title()
                days = int(input("Days: ").strip())
                # OPERATORS + CONDITIONAL + VALIDATION billing constraints
                if age < 0 or age > 120 or days < 0 or days > 365:
                    print("Invalid age/days!")
                elif ptype not in ["Inpatient","Outpatient"]:  # list + in operator
                    print("Type must be Inpatient/Outpatient")
                else:
                    patients.append([pid, name, age, ptype, dept, bpl, insurance, days, 0, 0, 0])  # nested list
                    print(f"Patient {name} added")  # f-string
            except:
                print("Enter valid numbers!")

    elif ch == "2":
        show_pattern("Calculate Bill")
        if len(patients) == 0:  # list
            print("No patients!")
        else:
            bills = []
            for p in patients:  # loop
                pid, name, age, ptype, dept, bpl, insurance, days, c1, c2, c3 = p  # UNPACKING 11 values
                print(f"\nBilling {pid} {name} Dept:{dept}")
                try:
                    consult = int(input(f"Consultation (base {500}): ").strip())
                    diag = int(input("Diagnostic: ").strip())
                    treat = int(input("Treatment: ").strip())
                    # VALIDATE billing constraints - OPERATORS
                    if consult < 0 or diag < 0 or treat < 0:
                        print("Charges cannot be negative!")
                        continue
                    if consult > 50000 or diag > 100000 or treat > 200000:
                        print("Charges too high! Validate!")
                        continue
                    subtotal = consult + diag + treat  # operator +
                    concession = calculate_concession(age, bpl, insurance, subtotal)  # fractions inside
                    total = subtotal - concession  # operator -
                    if total <= 0:  # validation
                        print("Invalid total <=0!")
                        continue
                    category, pay = classify_patient(total, concession, insurance)  # tuple unpacking 2
                    bills.append([pid, name, age, subtotal, concession, total, category, pay, dept, bpl])  # nested list
                    print(f"Sub={subtotal} Conc={concession:.2f} (fractions applied) Total={total:.2f} -> {category}/{pay}")
                except:
                    print("Enter valid numbers!")

    elif ch == "3":
        show_pattern("Bills")
        if len(bills) == 0:
            print("Calculate first!")
        else:
            print(f"{'ID':<6} {'Name':<10} {'Sub':<6} {'Conc':<6} {'Total':<6} {'Cat'}")
            for b in bills:
                pid, name, age, sub, conc, total, cat, pay, dept, bpl = b  # UNPACKING 10
                print(f"{pid:<6} {name:<10} {sub:<6} {conc:<6.0f} {total:<6.0f} {cat}/{pay}")

    elif ch == "4":
        show_pattern("Classification - Payment Policy")
        if len(bills) == 0:
            print("No bills!")
        else:
            print("Policy: High>50000, Medium>20000, Low<=20000")
            for b in bills:
                pid, name, age, sub, conc, total, cat, pay, dept, bpl = b
                print(f"{pid} {total:.0f} {cat} {pay} {dept}")

    elif ch == "5":
        show_pattern("Summary")
        if len(bills) == 0:
            print("No bills!")
        else:
            low = med = high = 0  # variables int
            total_sum = 0.0  # float
            for b in bills:  # loop
                pid, name, age, sub, conc, total, cat, pay, dept, bpl = b
                total_sum += total  # operator +=
                if cat == "Low":
                    low += 1
                elif cat == "Medium":
                    med += 1
                else:
                    high += 1
            avg = total_sum / len(bills)  # operator /
            print(f"Avg Rs.{avg:.2f} Low:{low} Med:{med} High:{high}")
            print("Pattern Chart:")
            for label, count in [("Low", low), ("Medium", med), ("High", high)]:  # list + tuple
                bar = "#" * count  # PATTERN GENERATION ### + operator *
                print(f"{label:<8}: {bar} ({count})")

    elif ch == "6":
        for i in range(5, 0, -1):  # PATTERN GENERATION + LOOP
            print("*" * i + " THANK YOU " + "*" * i)
        break
    else:
        print("Invalid choice!")
