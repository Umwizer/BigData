
#Ask under to insert this age 
#check age > 20
# ask for entering their height check height > 1.6 ask for number 
#check weight>45
#check physique slim,thick ,chubbby 
#ask for phoneumber and check if it is valid (10 digits)
#using if statment to check the above using if statement and print appropriate messages
#after all conditions are true let's say you are eligible to date me or yourenot according to the above conditions
age = int(input("Enter your age:"))
if(age < 20) :
   print("You are too young")
else:
  if(age > 20):
      print("You are old enough")
height = float(input("Enter your height in meters:"))
if(height < 1.6) :
   print("You are too short")
else:
  if(height > 1.6):
      print("You are tall enough")
weight = float(input("Enter your weight in kg:"))
if(weight < 45) :
   print("You are underweight")
else:
    if(weight > 45):
        print("You have a healthy weight")
physique = input("Enter your physique (slim, thick, chubby):").lower()
if physique == "slim":
    print("You have a slim physique")
elif physique == "thick":
    print("You have a thick physique")
elif physique == "chubby":
    print("You have a chubby physique")
else:    print("Invalid physique type")
phone_number = input("Enter your phone number (10 digits):")
if len(phone_number) == 10 and phone_number.isdigit():
    print("Valid phone number")
else:    print("Invalid phone number")
if age > 20 and height > 1.6 and weight > 45 and physique in ["slim", "thick", "chubby"] and len(phone_number) == 10 and phone_number.isdigit():
    print("You are eligible to date me")
else:
    print("You are not eligible to date me")