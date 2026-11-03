n = int(input("Enter number of passengers: "))

for i in range(n):

    print("\nEnter Passenger Details")

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))
    distance = float(input("Enter travel distance in km: "))

    print("\nSelect Travel Class")
    print("1. Sleeper - Rs. 1.5/km")
    print("2. AC 3 Tier - Rs. 2.5/km")
    print("3. AC 2 Tier - Rs. 3.5/km")

    choice = int(input("Enter class choice: "))

    if distance < 0 or age < 0:
        print("Invalid passenger details!")
        continue

    
    if choice == 1:
        rate = 1.5
        class_name = "Sleeper"

    elif choice == 2:
        rate = 2.5
        class_name = "AC 3 Tier"

    elif choice == 3:
        rate = 3.5
        class_name = "AC 2 Tier"

    else:
        print("Invalid class selection!")
        continue

    
    if distance <= 100:
        basic_fare = distance * rate

    elif distance <= 200:
        basic_fare = (100 * rate) + ((distance - 100) * rate * 1.10)

    else:
        basic_fare = (100 * rate) + (100 * rate * 1.10) + ((distance - 200) * rate * 1.20)

    
    if age < 5:
        concession = basic_fare
        basic_fare = 0

    elif age <= 12:
        concession = basic_fare * 0.50
        basic_fare = basic_fare - concession

    elif age >= 60:
        concession = basic_fare * 0.20
        basic_fare = basic_fare - concession

    else:
        concession = 0

    reservation_fee = 50

    ticket_fare = basic_fare + reservation_fee

    
    cancel = input("Cancel ticket? (yes/no): ").lower()

    if cancel == "yes":
        penalty = ticket_fare * 0.20
        refund = ticket_fare - penalty
        status = "Cancelled"

    else:
        penalty = 0
        refund = ticket_fare
        status = "Confirmed"

    
    print("\n------ RAILWAY FARE STATEMENT ------")
    print("Passenger Name:", name)
    print("Age:", age)
    print("Travel Class:", class_name)
    print("Distance:", distance, "km")
    print("Concession: Rs.", round(concession, 2))
    print("Reservation Fee: Rs.", reservation_fee)
    print("Ticket Fare: Rs.", round(ticket_fare, 2))
    print("Ticket Status:", status)
    print("Cancellation Penalty: Rs.", round(penalty, 2))
    print("Refund Amount: Rs.", round(refund, 2))
    print("-----------------------------------")

print("\nRailway Reservation Completed.")
