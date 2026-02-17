#Hello everyone, I'm going to do the basics, understand,
# and after that, you will be performing these mathematical 
# operations on it, where you will take this data, duplicate it,
# and you add five more elements in the second array, and later, 
# you will be finding the maximum, the minimum, and the average.
import numpy as np

import numpy as np

# Original array
data = np.array([10, 20, 30, 40, 50])

# Duplicate the array
new_data = data.copy()

# Add 5 more elements
new_elements = np.array([60, 70, 80, 90, 100])
new_data = np.concatenate((new_data, new_elements))

# Find maximum, minimum, and average
maximum = np.max(new_data)
minimum = np.min(new_data)
average = np.mean(new_data)

# Print results
print("Original data:", data)
print("New data:", new_data)
print("Maximum value:", maximum)
print("Minimum value:", minimum)
print("Average value:", average)


