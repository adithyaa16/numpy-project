from data_generator import generate_data
from analyzer import calculate_total, calculate_average, add_bonus, grade_students

# Generate dataset
marks = generate_data()

print("Original Marks:\n", marks)

# Apply broadcasting
updated_marks = add_bonus(marks)
print("\nAfter Bonus (Broadcasting):\n", updated_marks)

# Analysis
total = calculate_total(updated_marks)
avg = calculate_average(updated_marks)
grades = grade_students(avg)

print("\nTotal Marks:", total)
print("Average Marks:", avg)
print("Grades:", grades)