import numpy as np
from sys import getsizeof

arr = np.array([1, 7, 13, 105])
print(f"Memory occupied is {getsizeof(arr)} bytes")