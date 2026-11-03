students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks: "))
    subject = int(input("Enter minimum subject marks: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter family income: "))

    if (aggregate >= 75 and subject >= 60
            and attendance >= 75 and income <= 250000):

        students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

students.sort(key=lambda x: (
    -x["aggregate"],
    -x["attendance"],
    x["income"],
    x["name"].lower()
))

print("\n--- Scholarship Eligible Students ---")

if len(students) == 0:
    print("No eligible students found.")

else:
    for rank, student in enumerate(students, 1):
        print("\nRank:", rank)
        print("Name:", student["name"])
        print("Aggregate Marks:", student["aggregate"])
        print("Attendance:", student["attendance"])
        print("Family Income:", student["income"])

print("\nTotal Eligible Students:", len(students))
