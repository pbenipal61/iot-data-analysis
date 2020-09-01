import numpy as np

arr = np.random.randint(-20, 20, 20)
print(f"original array is {arr}")

flipped_arr = np.flip(arr)
print(f"reversed array is {flipped_arr}")