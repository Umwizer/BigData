
#add vectorization.
import numpy as np

print("Enter the name of shop:")
shop_name = input("Shop name: ")

# Step 1: Ask for age
age = int(input("Enter your age: "))

if age < 18 or age > 60:
    print("Application rejected. Age must be between 18 and 60.")
else:
    print("Age validated.")

    # Step 2: Ask for branch
    branch = input("Enter your branch (north/south/east/west): ").lower()

    while branch not in ['north', 'south', 'east', 'west']:
        print("Invalid branch. Please enter north, south, east, or west.")
        branch = input("Enter your branch (north/south/east/west): ").lower()

    print(f"Branch '{branch}' selected.")

    # Step 3: Ask for sales (keep asking if less than 100)
    sales = float(input("Enter your monthly sales amount: "))

    while sales < 100:
        print("Offer rejected. Sales are below 100.")
        sales = float(input("Please re-enter your monthly sales amount: "))

    print("Congratulations! You have high sales performance.")

    # Step 4: Regional sales overview using NumPy
    regional_sales = np.array([150, 200, 120, 300, 250, 50])

    maximum = np.max(regional_sales)
    minimum = np.min(regional_sales)
    average = np.mean(regional_sales)
    total = np.sum(regional_sales)

    print("\n--- Sales Overview by Region ---")
    print("Shop Name:", shop_name)
    print("Branch:", branch)
    print("Regional Sales:", regional_sales)
    print("Maximum Sales:", maximum)
    print("Minimum Sales:", minimum)
    print("Average Sales:", average)
    print("Total Sales:", total)


