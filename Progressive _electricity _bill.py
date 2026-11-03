

1. COMPUTATIONAL THINKING

*a) Decomposition:*
1.  Define consumption slabs
2.  Collect monthly data
3.  Calculate energy charge slab-wise
4.  Add fixed charge
5.  Apply surcharge (>300 units) and rebate (<100 units)
6.  Compare bills month-to-month
7.  Detect unusual increase and generate summary

*b) Pattern Recognition:*
- Slabs repeat: rate increases with units
- Bill formula same: Total = Energy + Fixed + Surcharge - Rebate
- Unusual increase pattern: percent > 30%

*c) Abstraction:*
- Bill = `[Month, Units, EnergyCharge, Fixed, Surcharge, Rebate, Total]`
- Slabs = `(start, end, rate)` 
- Monthly input = `[month_name, units]`

*d) Algorithm Design:* Rule-based + iterative loops

2. ALGORITHM (Step-by-step)
START
  STEP 1: Initialize slabs as tuple ((0,50,1.90), (51,100,3.0), (101,200,4.5), (201,300,6.0), (301,9999,8.0))
  STEP 2: Initialize fixed_charges tuple ((100,50), (200,80), (300,120), (9999,200))
  STEP 3: Initialize monthly_data=[] (nested list), bills=[] (nested list)
  STEP 4: Display menu in loop
  STEP 5: IF choice=1:
            Input month (string), units (int)
            Validate units 0-2000, check duplicate month using loop + string lower()
            Append [month, units] to monthly_data
  STEP 6: IF choice=2:
            FOR each data in monthly_data:
              Unpack month, units
              Calculate energy_charge using slab logic with IF conditions
              Get fixed charge by looping fixed_charges tuple
              IF units>500: surcharge=energy*0.15 ELIF units>300: surcharge=energy*0.10 ELSE 0
              IF units<100: rebate=energy*0.05 ELSE 0
              total=energy+fixed+surcharge-rebate
              Append [month,units,energy,fixed,surcharge,rebate,total] to bills
  STEP 7: IF choice=3: Display bills table using unpacking
  STEP 8: IF choice=4:
            FOR i=1 to len(bills)-1:
              prev_total=bills[i-1][6], curr_total=bills[i][6]
              diff=curr-prev, percent=diff/prev*100
              IF percent>30: UNUSUAL INCREASE ELSE Normal
  STEP 9: IF choice=5: Calculate average, highest, lowest using loops, display pattern chart
  STEP 10: IF choice=6: Pattern generation exit -> END
END
3. FLOWCHART
*Flowchart Symbols Used:*
- Oval: START/END
- Rectangle: Process (Initialize slabs tuple, Calculate energy)
- Diamond: Decision (Input choice?, units>300?, percent>30%?)
- Parallelogram: Input/Output (Display Menu, Input month)

4. PSEUDOCODE
SET slabs = ((0,50,1.90), (51,100,3.00), (101,200,4.50), (201,300,6.00), (301,9999,8.00))
SET fixed_charges = ((100,50), (200,80), (300,120), (9999,200))
SET monthly_data = []
SET bills = []

DEFINE get_fixed_charge(units):
  FOR max_u, charge IN fixed_charges:
    IF units <= max_u: RETURN charge

DEFINE calculate_energy_charge(units):
  energy=0, u=units
  IF u>300: energy+=(u-300)*8; u=300
  IF u>200: energy+=(u-200)*6; u=200
  IF u>100: energy+=(u-100)*4.5; u=100
  IF u>50: energy+=(u-50)*3; u=50
  IF units<=50: energy+=units*1.9 ELSE energy+=50*1.9
  RETURN energy

WHILE True:
  DISPLAY Menu 1.Add Month 2.Calculate 3.View 4.Compare 5.Summary 6.Exit
  READ choice
  IF choice==1:
    READ month STRING, units INT
    IF month length<3: PRINT invalid
    ELSE IF units<0 or >2000: PRINT invalid
    ELSE APPEND [month, units] TO monthly_data
  IF choice==2:
    FOR month, units IN monthly_data:
      energy=calculate_energy_charge(units)
      fixed=get_fixed_charge(units)
      IF units>500: surcharge=energy*0.15
      ELIF units>300: surcharge=energy*0.10
      ELSE surcharge=0
      IF units<100: rebate=energy*0.05 ELSE rebate=0
      total=energy+fixed+surcharge-rebate
      APPEND [month,units,energy,fixed,surcharge,rebate,total] TO bills
  IF choice==4:
    FOR i=1 TO len(bills)-1:
      percent=(bills[i][6]-bills[i-1][6])/bills[i-1][6]*100
      IF percent>30: PRINT "UNUSUAL INCREASE"
5. SYLLABUS CONCEPTS MAPPING - Every Item Covered

*a) Variables:* `month`, `units`, `energy`, `fixed`, `surcharge`, `rebate`, `total`, `slabs`, `bills`
*b) Data Types:* `int` (units), `float` (rate, energy), `string` (month), `list`, `tuple`
*c) Operators:* Arithmetic `+ - * / %`, Relational `> < <= >= == !=`, Logical `and or`, Assignment `+=`, Membership `in`
*d) Conditional Statements:* `if-elif-else` for slabs, surcharge, rebate, unusual detection
*e) Loops:* `while True` menu loop, `for` loop for slabs, `for i in range()` for comparison, nested loops
*f) Strings:* `strip()`, `title()`, `lower()`, `len()`, `in`, `f"{month}"` formatting
*g) Pattern Generation:*
for i in range(1,4): print("*"*i+" BILLING "+"*"*i)  # header
bar = "#"*int(total//100)  # chart
for i in range(5,0,-1): print("*"*i)
*h) Lists:* `monthly_data = []`, `bills = []`
*i) Nested Lists:* `monthly_data = [["Jan",80], ["Feb",150]]`, `bills = [[month, units, energy, fixed, surcharge, rebate, total]]`
*j) Tuples:* `slabs = ((0,50,1.90), ...)`, `fixed_charges = ((100,50), ...)`
*k) Tuple Operations:* `in` check `if loc in critical_locations`, iteration `for start,end,rate in slabs`, indexing `bills[0][6]`
*l) Unpacking:*
for start,end,rate in slabs:  # tuple unpacking
month, units = data
month, units, energy, fixed, sur, reb, total = b  # 7 values unpacking
max_u, charge = fixed_charges[0]
6. COMPLETE PYTHON SOLUTION - Strictly Syllabus Only
Progressive Electricity Billing System
Covers: variables, data types, operators, conditionals, loops, strings, pattern, lists, nested lists, tuples, tuple ops, unpacking

TUPLES - Slabs (start, end, rate)
slabs = (
    (0, 50, 1.90),
    (51, 100, 3.00),
    (101, 200, 4.50),
    (201, 300, 6.00),
    (301, 9999, 8.00)
)

TUPLES - Fixed charges (max_units, charge)
fixed_charges = (
    (100, 50),
    (200, 80),
    (300, 120),
    (9999, 200)
)

LISTS & NESTED LISTS
monthly_data = []  # [month_name, units] - nested list
bills = []  # [month, units, energy, fixed, surcharge, rebate, total] - nested list

VARIABLES + DATA TYPES + TUPLE OPERATIONS + UNPACKING
def get_fixed_charge(units):
    for max_u, charge in fixed_charges:  # tuple unpacking
        if units <= max_u:  # conditional + operators
            return charge
    return 200

def calculate_energy_charge(units):
    # VARIABLES float, int
    energy = 0.0
    u = units  # variable
    
    # CONDITIONAL STATEMENTS + OPERATORS
    if u > 300:
        energy += (u - 300) * 8.00  # operator *
        u = 300
    if u > 200:
        energy += (u - 200) * 6.00
        u = 200
    if u > 100:
        energy += (u - 100) * 4.50
        u = 100
    if u > 50:
        energy += (u - 50) * 3.00
        u = 50
    # OPERATORS + CONDITIONALS
    if units <= 50:
        energy += units * 1.90
    else:
        energy += 50 * 1.90
    return energy

def show_pattern(title):
    # PATTERN GENERATION + LOOPS + STRINGS
    print("\n" + "="*60)
    for i in range(1, 4):  # loop
        print("*" * i + " " + title + " " + "*" * i)  # string + pattern
    print("="*60)

MAIN MENU - WHILE LOOP
while True:
    show_pattern("ELECTRICITY BILLING")  # pattern generation
    print("1. Add Monthly Consumption")
    print("2. Calculate Bills")
    print("3. View All Bills")
    print("4. Compare Bills & Detect Unusual Increase")
    print("5. Summary Report")
    print("6. Exit")
    
    ch = input("Enter choice (1-6): ").strip()  # string
    
    # CONDITIONAL STATEMENTS
    if ch == "1":
        show_pattern("Add Consumption")
        month = input("Enter Month (e.g., Jan): ").strip().title()  # string operations
        if len(month) < 3:  # string + operator
            print("Invalid month name!")
        else:
            try:
                units = int(input("Enter Units (0-2000): ").strip())  # variable + data type int
                if units < 0 or units > 2000:  # operators
                    print("Units must be 0-2000")
                else:
                    exists = False
                    # LOOPS + NESTED LISTS + UNPACKING + STRINGS
                    for data in monthly_data:
                        m, u = data  # unpacking
                        if m.lower() == month.lower():  # string
                            exists = True
                            break
                    if exists:
                        print("Month already added!")
                    else:
                        monthly_data.append([month, units])  # nested list
                        print(f"Added {month} - {units} units")  # string
            except:
                print("Enter valid number!")
    
    elif ch == "2":
        show_pattern("Calculating Bills")
        if len(monthly_data) == 0:  # list + operator
            print("No monthly data! Add months first.")
        else:
            bills = []  # list
            # LOOP + UNPACKING + TUPLE OPERATIONS
            for data in monthly_data:
                month, units = data  # unpacking
                
                energy_charge = calculate_energy_charge(units)  # variable float
                fixed = get_fixed_charge(units)
                
                # CONDITIONAL + OPERATORS
                if units > 500:
                    surcharge = energy_charge * 0.15
                elif units > 300:
                    surcharge = energy_charge * 0.10
                else:
                    surcharge = 0.0
                
                if units < 100 and units > 0:  # operator and
                    rebate = energy_charge * 0.05
                else:
                    rebate = 0.0
                
                total = energy_charge + fixed + surcharge - rebate  # operators
                
                bills.append([month, units, energy_charge, fixed, surcharge, rebate, total])  # nested list
                print(f"{month}: Units={units}, TOTAL={total:.2f}")
            print("Bills calculated!")
    
    elif ch == "3":
        show_pattern("Bill Details")
        if len(bills) == 0:
            print("Calculate bills first!")
        else:
            print(f"{'Month':<10} {'Units':<7} {'Energy':<10} {'Fixed':<7} {'Surch':<7} {'Rebate':<7} {'Total'}")
            print("-"*70)
            # LOOP + UNPACKING 7 VALUES
            for b in bills:
                month, units, energy, fixed, sur, reb, total = b
                print(f"{month:<10} {units:<7} {energy:<10.2f} {fixed:<7} {sur:<7.2f} {reb:<7.2f} {total:.2f}")
    
    elif ch == "4":
        show_pattern("Bill Comparison")
        if len(bills) < 2:
            print("Need at least 2 months!")
        else:
            print(f"{'Month':<10} {'Total':<10} {'Change':<15} {'Status'}")
            print("-"*60)
            prev_month, prev_units, prev_e, prev_f, prev_s, prev_r, prev_total = bills[0]  # unpacking
            print(f"{prev_month:<10} {prev_total:<10.2f} {'-':<15} BASE")
            
            unusual_found = False
            # LOOP + NESTED LIST INDEXING
            for i in range(1, len(bills)):
                month, units, energy, fixed, sur, reb, total = bills[i]
                prev_month, prev_units, prev_e, prev_f, prev_s, prev_r, prev_total = bills[i-1]
                
                diff = total - prev_total  # operator
                percent = (diff / prev_total) * 100 if prev_total != 0 else 0  # operator
                
                # CONDITIONAL
                if percent > 30:
                    status = "UNUSUAL INCREASE!"
                    unusual_found = True
                elif percent > 15:
                    status = "High Increase"
                elif percent < 0:
                    status = "Decrease"
                else:
                    status = "Normal"
                
                print(f"{month:<10} {total:<10.2f} {diff:+.2f} ({percent:+.1f}%) {status}")
            
            if unusual_found:
                print("\n*** ALERT: Unusual increase detected! ***")
            else:
                print("\nNo unusual increases.")
    
    elif ch == "5":
        show_pattern("Summary Report")
        if len(bills) == 0:
            print("No bills!")
        else:
            total_sum = 0.0
            highest = bills[0]
            lowest = bills[0]
            
            # LOOPS to find highest, lowest, average
            for b in bills:
                month, units, energy, fixed, sur, reb, total = b  # unpacking
                total_sum += total  # operator +=
                if total > highest[6]:  # tuple operation indexing nested list
                    highest = b
                if total < lowest[6]:
                    lowest = b
            
            avg = total_sum / len(bills)  # operator /
            
            print(f"Total Months: {len(bills)}")
            print(f"Average Bill: Rs. {avg:.2f}")
            h_month, h_units, h_e, h_f, h_s, h_r, h_total = highest  # unpacking
            l_month, l_units, l_e, l_f, l_s, l_r, l_total = lowest
            print(f"Highest: {h_month} Rs.{h_total:.2f} ({h_units} units)")
            print(f"Lowest: {l_month} Rs.{l_total:.2f} ({l_units} units)")
            
            # PATTERN GENERATION chart
            print("\nBill Amount Chart (Pattern):")
            for b in bills:
                month, units, energy, fixed, sur, reb, total = b
                bar_len = int(total // 100)  # operator //
                if bar_len > 20:
                    bar_len = 20
                bar = "#" * bar_len  # pattern generation
                print(f"{month:<8}: {bar} Rs.{total:.0f}")
            
            # TUPLE OPERATIONS
            print("\nSlab-wise Consumption:")
            for start, end, rate in slabs:  # tuple unpacking
                count = 0
                for data in monthly_data:  # nested list loop
                    m, u = data
                    if u >= start and u <= end:
                        count += 1
                print(f"{start}-{end} @ Rs.{rate}: {count} month(s)")
    
    elif ch == "6":
        # PATTERN GENERATION exit
        for i in range(5, 0, -1):
            print("*" * i + " THANK YOU " + "*" * i)
        print("Exiting Billing System - Save Electricity!")
        break
    
    else:
        print("Invalid choice! Enter 1-6")
