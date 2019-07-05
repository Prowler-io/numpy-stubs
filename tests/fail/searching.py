import numpy as np

int_list = np.arange(10)


np.where(int_list < 5, -1)  # E: No overload variant
