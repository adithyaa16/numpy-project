import numpy as np

def calculate_total(marks):
    return np.sum(marks, axis=1)

def calculate_average(marks):
    return np.mean(marks, axis=1)

def add_bonus(marks):
    bonus = np.array([5, 5, 5])   # broadcasting
    return marks + bonus

def grade_students(avg):
    grades = []
    for a in avg:
        if a >= 85:
            grades.append("A")
        elif a >= 70:
            grades.append("B")
        else:
            grades.append("C")
    return grades