

# Write program to:
# 1. Check if number is even/odd
# 2. Print multiplication table (1-10) for a given number
# 3. Find all prime numbers between 1 and 50

# Check if number is even/odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
    
# Print multiplication table (1-10) for a given number
num_for_table = int(input("Enter a number to see its multiplication table: "))
print(f"Multiplication Table for {num_for_table}:")
for i in range(1, 11):
    print(f"{num_for_table} x {i} = {num_for_table * i}")
# Find all prime numbers between 1 and 50
print("Prime numbers between 1 and 50:")
for num in range(2, 51):
    is_prime = True
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
        