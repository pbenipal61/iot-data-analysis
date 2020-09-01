import numpy as np

arr = np.array([i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0] )
print(f"array is {arr}")

sum = np.sum(arr)
print(f"sum is {sum}")