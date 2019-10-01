import numpy as np

np.datetime64('2001') + np.datetime64('2002')  # E: Unsupported operand types for + ("datetime64" and "datetime64")
np.timedelta64(1) - np.datetime64('2001')  # E: Unsupported operand types for - ("timedelta64" and "datetime64")