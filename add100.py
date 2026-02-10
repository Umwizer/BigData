#numbers = [45, 23, 67, 12, 89, 34, 56, 78]
# Find: maximum, minimum, sum, average
# Add 100 to the list
# Sort in descending order
# Create new list with only numbers > 50 using list comprehension


numbers = [45,23,67,12,89,34,56,78]

# maximum,minimum,sum,average
maximum = max(numbers)
minimum = min(numbers)
total_sum = sum(numbers)
average = total_sum / len(numbers)

print("Numbers:", numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total_sum)
print("Average:", average)

# adding a new number to the list
numbers.append(100)
print("Updated List:", numbers)

# filtering numbers greater than 50
numbers_above_50 = [num for num in numbers if num > 50]
print("Numbers above 50:", numbers_above_50)