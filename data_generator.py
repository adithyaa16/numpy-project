import numpy as np

def generate_data(num_students=5):
    # Random marks (3 subjects)
    marks = np.random.randint(40, 100, size=(num_students, 3))
    return marks