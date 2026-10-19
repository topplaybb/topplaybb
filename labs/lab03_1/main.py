# Starting file for LAB 3-1

print("The Miles Per Gallon program")
print()

another_trip = "y"

while another_trip.lower() == "y":
    miles = float(input("Enter miles driven: "))
    gallons = float(input("Enter gallons of gas used: "))
    cost_per_gallon = float(input("Enter cost per gallon: "))

    if miles > 0 and gallons > 0 and cost_per_gallon > 0:
        mpg = round(miles / gallons, 2)
        total_gas_cost = round(gallons * cost_per_gallon, 2)
        cost_per_mile = round(total_gas_cost / miles, 2)

        print(f"Miles Per Gallon: {mpg}")
        print(f"Total Gas Cost: {total_gas_cost}")
        print(f"Cost Per Mile {cost_per_mile}")
    else:
        print("All entries must be greater than zero. Try again.")

    print()
    another_trip = input("Get entries for another trip (y/n)? ")
    print()

print("Bye!")