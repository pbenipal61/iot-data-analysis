import numpy as np

arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])
arr = np.add(arrayOne, arrayTwo)
rooted_arr = np.sqrt(arr)
print(f"sum of matrices is {arr}")
print(f"square root of sum matrices is {rooted_arr}")