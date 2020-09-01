import numpy as np

array_one = np.array([[5, 6, 9], [21, 18, 27]])
array_two = np.array([[15, 33, 24], [4, 7, 1]])
sample_array = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

print(f"sorted by second row {array_one[:, array_one[1].argsort()]}")
print(f"sorted by second column {array_two[array_two[:, 1].argsort(), : ]}")
print(f"sorted {np.sort(sample_array)}")

