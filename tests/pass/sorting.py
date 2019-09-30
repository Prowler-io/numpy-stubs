import numpy as np

int_list = [1, 2, 3, 4]
int_array = np.array(int_list)
structured = np.array([('a', 2), ('c', 1)], dtype=[('x', 'S1'), ('y', int)])

# ndarray sorting method
int_array.sort()
structured.sort(axis=0, kind="quicksort", order='x')
structured.sort(axis=0, kind="quicksort", order=('x', 'y'))

# Floating sorting methods
np.sort(int_list)
np.sort(int_array)
np.sort(structured, axis=0, kind="quicksort", order='x')
np.sort(structured, axis=0, kind="quicksort", order=('x', 'y'))

np.lexsort(structured, axis=0)
np.lexsort((['Alice', 'Bob'], [1, 2]), axis=0)

np.argsort(int_list, kind="quicksort", axis=None)
np.argsort(int_list, kind="quicksort", axis=0)
np.argsort(structured, kind="quicksort", order='x')
np.argsort(structured, kind="quicksort", order=('x', 'y'))

np.msort(int_list)
np.msort(int_array)

np.sort_complex(int_list)
np.sort_complex(int_array)

np.partition(int_list, kind="introselect", kth=1)
np.partition(int_list, kind="introselect", kth=(1, 3))
np.partition(int_list, kind="introselect", kth=1, axis=None)
np.partition(int_list, kind="introselect", kth=1, axis=0)
np.partition(int_list, kind="introselect", kth=1, order=None)
np.partition(structured, kind="introselect", kth=1, order='x')
np.partition(structured, kind="introselect", kth=1, order=('x', 'y'))
