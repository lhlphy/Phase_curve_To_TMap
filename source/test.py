import os
import numpy as np

file_path = 'data/pc_theory.txt'
if os.path.exists(file_path):
    data = np.loadtxt(file_path, delimiter=',')
    x_data = data[:, 0]
    y_data = data[:, 1]
    print(x_data)
else:
    print(f"File {file_path} does not exist.")