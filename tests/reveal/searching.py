import numpy as np

int_matrix = np.ones(5, 5)
target = np.ones(5)

reveal_type(np.argmax(int_matrix))  # E: numpy.int64
reveal_type(np.argmax(int_matrix, axis=None))  # E: numpy.int64
reveal_type(np.argmax(int_matrix, axis=0))  # E: numpy.ndarray
reveal_type(np.argmax(int_matrix, axis=0, out=target))  # E: numpy.ndarray

reveal_type(np.argmin(int_matrix))  # E: numpy.int64
reveal_type(np.argmin(int_matrix, axis=None))  # E: numpy.int64
reveal_type(np.argmin(int_matrix, axis=0, out=target))  # E: numpy.ndarray
