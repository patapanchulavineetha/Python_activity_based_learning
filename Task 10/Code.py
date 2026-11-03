n = int(input("Enter number of patients: "))

for i in range(n):

    print("\nEnter Patient Details")

    name = input("Enter patient name: ")
    patient_id = input("Enter patient ID: ")

    consultation = float(input("Enter consultation charges: "))
    diagnostic = float(input("Enter diagnostic charges: "))
    treatment = float(input("Enter treatment charges: "))

    
    if consultation < 0 or diagnostic < 0 or treatment < 0:
        print("Invalid charges! Please enter positive values.")
        continue

    
    total = consultation + diagnostic + treatment

    
    if total > 10000:
        concession = total * 0.10
    else:
        concession = 0

    final_bill = total - concession

    
    if final_bill < 5000:
        category = "Low Payment"

    elif final_bill <= 15000:
        category = "Medium Payment"

    else:
        category = "High Payment"

    
    print("\n--- Hospital Bill ---")
    print("Patient Name:", name)
    print("Patient ID:", patient_id)
    print("Consultation Charges:", consultation)
    print("Diagnostic Charges:", diagnostic)
    print("Treatment Charges:", treatment)
    print("Total Bill: Rs.", total)
    print("Concession: Rs.", concession)
    print("Final Bill: Rs.", final_bill)
    print("Patient Category:", category)

print("\nHospital Billing Completed.")
