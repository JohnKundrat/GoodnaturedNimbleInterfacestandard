# Prompt user with the Car Shop Welcome Screen
print("=" * 32)
print("  Welcome to the UMBC Car Shop!")
print("=" * 32)
print("")

# Ask the user questions to customize their car and assign to a  variable

#Question 1

print("~Make and Model~")
print("")
print("1. What Model of Car are you Ordering?")
print("  a. Lightning Speedster")
print("  b. Eco Leaf")
print("  c. Harp Chord")
print("  d. Chevron")
carMake = input("Please enter (a) - (d): ")
print("")

# Question 2

print("2. Would you like to upgrade from the 4-door option to the 2-door option?")
carDoorUpgrade = input("Please enter 'yes' or' 'no': ")
print("")

# Question 3

print(" ~ Exterior ~")
print("")
print("3. What color would you like your car to be?")
carColor = input("You may enter the name of any color you'd like: ")
print("")

# Question 4

print("4. Would you like the deluxe weather package?")
carWeatherPackage = input("Please enter 'yes' or 'no': ")
print("")

#Question 5

print("~ Interior~")
print("")
print("5. Which Engine would you like your car to have?")
print("  a. I-4 Entry Engine")
print("  b. V-6 Performance Engine")
print("  c. Eco Diesel Engine")
carEngine = input("Please enter (a) - (c): ")
print("")

#Question 6

print("6. Would you like heated seats?")
carHeatedSeats = input("Please enter 'yes' or 'no': ")
print("")

#Print out summary

print("=" * 32)
print("~ Summary ~")
print(f"Model Option: {carMake}")
print(f"Upgrade to 2-Door: {carDoorUpgrade}")
print(f"Desired Color: {carColor}")
print(f"Upgrade to Deluxe Weather: {carWeatherPackage}")
print(f"Engine Option: {carEngine}")
print(f"Upgrade to Heated Seats: {carHeatedSeats}")
