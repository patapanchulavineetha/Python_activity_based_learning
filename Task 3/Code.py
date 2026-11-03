n = int(input("Enter number of employees: "))

for i in range(n):

    print("\nEnter Employee Details")

    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")

    basic = float(input("Enter basic salary: "))
    allowances = float(input("Enter allowances: "))
    overtime_hours = float(input("Enter overtime hours: "))
    overtime_rate = float(input("Enter overtime rate: "))
    incentives = float(input("Enter incentives: "))
                             
    if (basic < 0 or allowances < 0 or
        overtime_hours < 0 or overtime_rate < 0 or
        incentives < 0):

        print("Invalid salary details!")
        continue

    
    overtime_pay = overtime_hours * overtime_rate

  
    gross = basic + allowances + overtime_pay + incentives

    
    if gross <= 20000:
        deduction = 0

    elif gross <= 40000:
        deduction = gross * 0.05

    else:
        deduction = gross * 0.10

    
    net_salary = gross - deduction
  
    print("\n------ SALARY STATEMENT ------")
    print("Employee Name:", name)
    print("Employee ID:", emp_id)
    print("Basic Salary: Rs.", basic)
    print("Allowances: Rs.", allowances)
    print("Overtime Pay: Rs.", overtime_pay)
    print("Incentives: Rs.", incentives)
    print("Gross Salary: Rs.", gross)
    print("Deduction: Rs.", deduction)
    print("Net Salary: Rs.", net_salary)
    print("------------------------------")

print("\nPayroll Processing Completed.")
