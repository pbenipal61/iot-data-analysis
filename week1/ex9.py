import numpy as np

arr = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

max_on_0 = np.amax(arr, axis=0)

min_on_1 = np.amin(arr, axis=1)

print(f"max on axis 0 is {max_on_0}")
print(f"min on axis 1 is {min_on_1}")