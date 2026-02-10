for person in range(1, 4):
    print(f"\n--- Person {person} ---")

    age = int(input("Enter your age: "))
    if age > 20:
        age_ok = True
        age_app = True
        print("Age OK")
    elif 18 <= age <= 20:
        age_ok = False
        age_app = True
        print("You are allowed to join the dating app, but not eligible to date me")
    else:
        age_ok = False
        age_app = False
        print("You are too young")

    height = float(input("Enter your height in meters: "))
    if height > 1.6:
        height_ok = True
        print("Height OK")
    else:
        height_ok = False
        print("Too short")

    weight = float(input("Enter your weight in kg: "))
    if weight > 45:
        weight_ok = True
        print("Weight OK")
    else:
        weight_ok = False
        print("Underweight")

    physique = input("Enter your physique (slim, thick, chubby): ").lower()
    if physique == "slim" or physique == "thick" or physique == "chubby":
        physique_ok = True
        print("Physique OK")
    else:
        physique_ok = False
        print("Invalid physique")

    phone = input("Enter your phone number (10 digits): ")
    if len(phone) == 10 and phone.isdigit():
        phone_ok = True
        print("Phone number OK")
    else:
        phone_ok = False
        print("Invalid phone number")

    # Final decision
    if age_ok and height_ok and weight_ok and physique_ok and phone_ok:
        print(" You are eligible to date me")
    elif age_app and height_ok and weight_ok and physique_ok and phone_ok:
        print("ℹ You can join the dating app")
    else:
        print("You are not eligible")
