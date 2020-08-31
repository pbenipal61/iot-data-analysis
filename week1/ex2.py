import numpy as np


def arr_has_0_check(int_arr) -> bool:
    """
    Check if an array contains an element as 0
    :param int_arr: Array
    :return: True/False
    """
    return 0 in int_arr


arr = np.random.randint(-20, 20, 20)
print(arr_has_0_check(arr))


