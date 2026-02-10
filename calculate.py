
# Write function: calculate_statistics(numbers)
# Should return: mean, median, max, min as a tuple
# Test with: [12, 45, 67, 23, 89, 34, 56, 78,90,21]


def calculate_statistics(numbers):
    # calculate mean
    mean = sum(numbers) / len(numbers)
    
    # calculate median (corrected for both odd and even length lists)
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 1:  # odd length
        median = sorted_nums[n // 2]
    else:  # even length
        median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    
    # calculate max and min
    maximum = max(numbers)
    minimum = min(numbers)
    
    return mean, median, maximum, minimum

# Test
test_numbers = [12, 45, 67, 23, 89, 34, 56, 78, 90, 21]
mean, median, maximum, minimum = calculate_statistics(test_numbers)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")