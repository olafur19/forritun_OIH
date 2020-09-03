

base_b = 40
mile_b = 0.25
base_d = 60
mile_d = 0.25

print("Welcome to car rentals!")
check = input("Would you like to continue (y/n)? ")
while check == "y":
    code = input("Customer code (b or d): ")
    if code == "b":
        days = float(input("Number of days: "))
        odo_start = int(input("Odometer reading at the start: "))
        odo_end = int(input("Odometer reading at the end: "))
        totalmiles = odo_end - odo_start
        cost = (days * base_b) + (totalmiles * mile_b)
        print("Miles driven:", totalmiles)
        print("Amount due:", round(cost, 1))
        check = input("Would you like to continue (y/n)? ")
    elif code == "d":
        days = float(input("Number of days: "))
        odo_start = int(input("Odometer reading at the start: "))
        odo_end = int(input("Odometer reading at the end: "))
        totalmiles = odo_end - odo_start
        daily = days * 100                  #Free miles per day
        miles_due = totalmiles - daily      #payment for extra miles
        cost = (days * base_d) + (miles_due * mile_d)
        print("Miles driven:", totalmiles)
        print("Amount due:", round(cost, 1))
        check = input("Would you like to continue (y/n)? ")