# Create dictionary: 5 students with names and test scores (list of 3 scores each)
# Calculate average score for each student
# Find student with highest average
# Add a new student with scores

students ={
    "Alice": [85, 90, 78],
    "Ange": [92, 88, 95],
    "Rene": [70, 75, 80],
    "Ruth": [88, 82, 91],
    "John": [80, 85, 87]
}

# calculate average score for each student
averages ={}
for student, scores in students.items():
    averages[student] = sum(scores) / len(scores)
    
print("Average Scores:",averages)

# find student with highest average
highest_avg_student = max(averages, key=averages.get)
print("Student with highest average:", highest_avg_student) 