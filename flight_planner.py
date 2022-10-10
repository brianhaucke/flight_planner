# Flight Planner
logo = """          ******************************************************
          *                     PYTHON AIR                     *
          ******************************************************
                        """

spacer = "******************************************"

passengers = 0
depart_num = 0
arrive_num = 0
# Choose checking bags
bag_check = False
check_bags = 0

print(logo)
print("Welcome to Python Air, with non-stop service to 6 different big cities!")
print(spacer)

#How many passengers
while passengers == 0:
    try:
        passengers = int(input("How many passengers: "))
    except ValueError:
        print("Please enter a valid number")

# Choose a Departure City
depart = input("Please enter the first letter of your departure city: (S)eattle, (D)allas, (L)os Angeles, (N)ew York, (M)iami, (C)hicago: ").lower()
if depart == "s":
    depart_num = 1
    depart_name = "Seattle"
elif depart == "d":
    depart_num = 2
    depart_name = "Dallas"
elif depart == "l":
    depart_num = 3
    depart_name = "Los Angeles"
elif depart == "n":
    depart_num = 4
    depart_name = "New York"
elif depart == "m":
    depart_num = 5
    depart_name = "Miami"
elif depart == "c":
    depart_num = 6
    depart_name = "Chicago"
else:
    print("Error: Not a valid departure city")
    quit()

# Choose an arrival City
arrive = input("Please enter the first letter of your arrival city: (S)eattle, (D)allas, (L)os Angeles, (N)ew York, (M)iami, (C)hicago: ").lower()
if arrive == depart:
    print("Error: Arrival and Destination are the same city. Please try again.")
    quit()
if arrive == "s":
    arrive_num = 1
    arrive_name = "Seattle"
elif arrive == "d":
    arrive_num = 2
    arrive_name = "Dallas"
elif arrive == "l":
    arrive_num = 3
    arrive_name = "Los Angeles"
elif arrive == "n":
    arrive_num = 4
    arrive_name = "New York"
elif arrive == "m":
    arrive_num = 5
    arrive_name = "Miami"
elif arrive == "c":
    arrive_num = 6
    arrive_name = "Chicago"
else:
    print("Error: Not a valid arrival city")
    quit()

# Choose first class, business, or economy class
level = input("Would you like to fly First Class, Business Class, or Economy Class (Type F, B, or E): ").lower()

# Choose checking bags
while bag_check == False:
    try:
        check_bags = int(input("How many bags will you be checking: "))
        bag_check = True
    except ValueError:
        print("Your input was not a valid number")

# flight planner function -> calculates the cost of the flight, plus any bag charges and upgrades
def flight_planner(passengers, depart_num, arrive_num, level, check_bags):
    flight_cost = 0
    class_charge = 0
    level_name = "Economy"
    bag_fee = 35
    total_bag_fee = check_bags * bag_fee
    if level == "f":
        class_charge = 200
        level_name = "First"
    elif level == "b":
        class_charge = 90
        level_name = "Business"

    da_total = depart_num + arrive_num
    if da_total == 3:
        flight_cost = 150
    elif da_total == 4:
        flight_cost = 175
    elif da_total == 5:
        flight_cost = 200
    elif da_total == 6:
        flight_cost = 225
    elif da_total == 7:
        flight_cost = 250
    elif da_total == 8:
        flight_cost = 275
    elif da_total == 9:
        flight_cost = 280
    elif da_total == 10:
        flight_cost = 300
    elif da_total == 11:
        flight_cost = 325
    # Display the flight cost, and a breakdown of extra fees (first class, bags)
    print(spacer)
    print("Your Flight from " + depart_name + " to " + arrive_name)
    print("Total # of Passengers: " + str(passengers))
    print(" -- Flight cost: $" + str(flight_cost * passengers))
    if passengers > 1:
        print("     -- $" + str(flight_cost) + " per passenger" )
    if level_name != "Economy":
        print(" -- " + level_name + " class upgrade charge: $" + str(class_charge * passengers))
        if passengers > 1:
            print("     -- $" + str(class_charge) + " per passenger")

    if bag_fee != 0:
        print(" -- " + "Checked Bag fee: $" + str(total_bag_fee))
        print("     -- $" + str(bag_fee) + " per bag")

    # Calculate everything
    total_cost = (flight_cost * passengers) + (class_charge * passengers) + total_bag_fee
    # Print out the total cost
    print("Your total cost (before taxes) is: $" + str(total_cost))
    print(spacer)

flight_planner(passengers, depart_num, arrive_num, level, check_bags)
