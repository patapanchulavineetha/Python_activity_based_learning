import math

print("CAMPUS EVENT FINANCIAL PLANNING")


participants = int(input("Enter expected participants: "))

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))

catering = float(input("Enter catering cost per participant: "))
transport = float(input("Enter transport cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

sponsorship = float(input("Enter sponsorship amount: "))
registration_fee = float(input("Enter registration fee per participant: "))


if (participants <= 0 or venue < 0 or equipment < 0
        or catering < 0 or transport < 0
        or certificate < 0 or sponsorship < 0
        or registration_fee < 0):

    print("Invalid input details!")

else:

    
    fixed_cost = venue + equipment

    variable_cost = catering + transport + certificate

    
    catering_total = catering * participants
    transport_total = transport * participants
    certificate_total = certificate * participants

    
    total_cost = (fixed_cost +
                  catering_total +
                  transport_total +
                  certificate_total)

    
    contributions = registration_fee * participants

  
    shortfall = max(0, total_cost - sponsorship - contributions)

   
    balance = registration_fee - variable_cost

    if sponsorship >= fixed_cost:
        break_even = 0

    elif balance > 0:
        break_even = math.ceil(
            (fixed_cost - sponsorship) / balance
        )

    else:
        break_even = None

    
    print("\n------ CAMPUS EVENT FINANCIAL REPORT ------")

    print("Expected Participants:", participants)

    print("\n--- Event Expenses ---")
    print("Venue Cost: Rs.", venue)
    print("Equipment Cost: Rs.", equipment)
    print("Catering Cost: Rs.", catering_total)
    print("Transport Cost: Rs.", transport_total)
    print("Certificate Cost: Rs.", certificate_total)

    print("\nTotal Event Cost: Rs.", total_cost)

    print("\n--- Financial Details ---")
    print("Sponsorship: Rs.", sponsorship)
    print("Participant Contributions: Rs.", contributions)
    print("Registration Fee: Rs.", registration_fee)

    print("Sponsorship Shortfall: Rs.", shortfall)

    if break_even is not None:
        print("Minimum Registrations for Break-even:",
              break_even)
    else:
        print("Break-even cannot be achieved with the given fee.")

    
    if shortfall == 0:
        print("Financial Status: Budget Covered")
    else:
        print("Financial Status: Additional Funds Required")

    print("\nProgram Completed.")
