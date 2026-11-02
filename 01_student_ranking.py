
Here iion* for Case Study 01 as per your syllabus instructions. You

*1. Computational Thinking:*
Decomposition: Divide into Evaluation + Ranking + Tie Breaking
Pattern: Same criteria check for all students
Abstraction: Only need Name, Marks List, Attendance, Income
Algorithm: Loop -> Check Conditions -> Bubble Sort for Ranking

*2. Algorithm:*
START
INPUT: List of Students
ELIGIBLE = []
FOR each student:
  CALC aggregate
  IF aggregate>=75 AND each subject>=60 AND attendance>=75 AND income<=300000:
    ADD to ELIGIBLE
SORT ELIGIBLE by: Aggregate DESC, Attendance DESC, Income ASC, Name ASC
PRINT ELIGIBLE with Ranks
END
*3. Flowchart:*
`Start -> Input Students -> Take One Student -> Calculate Aggregate -> All 4 Conditions Satisfied? -> NO: Mark Not Eligible -> YES: Add to Eligible List -> More Students? YES: Next Student -> NO: Sort List by Rules -> Display Rank List -> End`

*4. Pseudocode:*
FOR student IN students:
  total=0, fail=False
  FOR m IN marks: total+=m; IF m<60 fail=True
  aggregate=total/3
  IF aggregate>=75 AND fail==False AND attendance>=75 AND income<=300000:
    eligible.append((name, aggregate, attendance, income))
SORT eligible using bubble sort with tie logic
*5. Complete Python Program - Syllabus Only*
Case Study 01: University Scholarship Allocation
Concepts: variables, data types, operators, conditionals, loops, 
strings, lists, nested lists, tuples, tuple operations, unpacking

--- Input Data using Nested List ---
Format: [Name, [Sub1, Sub2, Sub3], Attendance, Income]
students = [
    ["Anjali", [82, 78, 85], 88, 200000],
    ["Ravi", [90, 92, 88], 90, 250000],
    ["Priya", [75, 80, 77], 76, 150000],
    ["Amit", [78, 55, 80], 85, 200000],      # Fail: Subject < 60
    ["Sneha", [88, 89, 85], 92, 280000],
    ["Vijay", [82, 78, 85], 88, 180000],      # Tie case with Anjali
    ["Karan", [70, 72, 74], 80, 100000]       # Fail: Aggregate < 75
]

eligible = []  # List to store tuples

--- Evaluation using Loops and Conditionals ---
print("--- Evaluation Phase ---")
for student in students:
    # Unpacking
    name, marks, attendance, income = student
    
    total = 0
    subject_failed = False
    
    # Loop for aggregate and subject-wise check
    for m in marks:
        total = total + m
        if m < 60:
            subject_failed = True
    
    aggregate = total / len(marks)
    
    # Conditional Statements with Operators
    if aggregate >= 75 and subject_failed == False and attendance >= 75 and income <= 300000:
        # Tuple Operations
        record = (name, aggregate, attendance, income)
        eligible.append(record)
        print(f"{name}: ELIGIBLE")
    else:
        print(f"{name}: NOT ELIGIBLE - Agg:{aggregate:.1f}")

--- Ranking using Bubble Sort and Tuple Unpacking ---
n = len(eligible)
for i in range(n):
    for j in range(0, n - i - 1):
        # Unpacking for comparison
        name1, agg1, att1, inc1 = eligible[j]
        name2, agg2, att2, inc2 = eligible[j+1]
        
        should_swap = False
        
        # Tie Breaking Rules
        if agg1 < agg2:
            should_swap = True
        elif agg1 == agg2:
            if att1 < att2:
                should_swap = True
            elif att1 == att2:
                if inc1 > inc2:
                    should_swap = True
                elif inc1 == inc2:
                    # String comparison for alphabetical order
                    if name1 > name2:
                        should_swap = True
        
        if should_swap:
            temp = eligible[j]
            eligible[j] = eligible[j+1]
            eligible[j+1] = temp

--- Output with String and Pattern Generation ---
print("\n" + "=" * 45)
title = " FINAL SCHOLARSHIP RANK LIST "
print(title.center(45, "*"))
print("=" * 45)

rank = 1
for rec in eligible:
    name, agg, att, inc = rec  # Unpacking
    # String formatting
    print(f"Rank {rank} -> {name} | Agg: {agg:.2f} | Att: {att}% | Income: Rs.{inc}")
    rank = rank + 1

print("=" * 45)
*File Name to use in GitHub:*
`01_scholarship_allocation.py
