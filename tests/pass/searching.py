import numpy as np

int_list = np.arange(10)
int_matrix = np.array([[0, 1], [1, 0]])
target = np.zeros_like([0, 0])

np.argmin(int_matrix, axis=None, out=None)
np.argmin(int_matrix, axis=-1, out=target)
np.nanargmin(int_matrix, axis=None)

np.argmax(int_matrix, axis=None, out=None)
np.argmax(int_matrix, axis=-1, out=target)
np.nanargmax(int_matrix, axis=None)

np.argwhere(int_matrix == 0)
np.nonzero(int_matrix)
np.flatnonzero(int_matrix)
np.where(int_matrix > 0, -np.ones_like(int_matrix), np.ones_like(int_matrix))
np.searchsorted(int_list, [1, 3], side="right")
np.searchsorted(int_list, 1, side="right")
np.extract(int_list < 5, int_list * 10)
np.count_nonzero(int_matrix, axis=None)
np.count_nonzero(int_matrix, axis=0)
np.count_nonzero(int_matrix, axis=(0, 1))
