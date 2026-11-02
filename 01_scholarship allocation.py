# University Scholarship Allocation System

# Data: [Name, [Marks List], Attendance %, Income]
students = [
    ["Anjali", [82, 78, 85], 88, 200000],
    ["Ravi", [90, 92, 88], 90, 250000],
    ["Priya", [75, 80, 77], 76, 150000],
    ["Amit", [78, 55, 80], 85, 200000],
    ["Sneha", [88, 89, 85], 92, 280000],
    ["Vijay", [82, 78, 85], 88, 180000],
    ["Karan", [70, 72, 74], 80, 100000]
]

eligible = []

# Step 1: Check Eligibility
for s in students:
    name, marks, attendance, income = s
    
    total = 0
    all_subject_pass = True
    for m in marks:
        total += m
        if m < 60:
            all_subject_pass = False
            
    aggregate = total / len(marks)
    
    if aggregate >= 75 and all_subject_pass == True and attendance >= 75 and income <= 300000:
        # Tuple: (name, aggregate, attendance, income)
        eligible.append((name, aggregate, attendance, income))
    else:
        print(f"{name} - Not Eligible (Agg: {aggregate:.1f})")

# Step 2: Ranking - Bubble Sort
# Rule: High Aggregate > High Attendance > Low Income > Name A-Z
n = len(eligible)
for i in range(n):
    for j in range(n - i - 1):
        name1, agg1, att1, inc1 = eligible[j]
        name2, agg2, att2, inc2 = eligible[j+1]
        
        swap = False
        if agg1 < agg2:
            swap = True
        elif agg1 == agg2:
            if att1 < att2:
                swap = True
            elif att1 == att2:
                if inc1 > inc2:
                    swap = True
                elif inc1 == inc2:
                    if name1 > name2:
                        swap = True
        if swap:
            temp = eligible[j]
            eligible[j] = eligible[j+1]
            eligible[j+1] = temp

# Step 3: Final Result
print("\n--- Final Scholarship Rank List ---")
rank = 1
for rec in eligible:
    name, agg, att, inc = rec
    print(f"Rank {rank}: {name} | Agg: {agg:.2f} | Att: {att}% | Income: {inc}")
    rank += 1

print("\n" + "*" * 35)
print("SCHOLARSHIP RESULT".center(35))
print("*" * 35)
