import numpy as np
my_array = np.array([1, 2, 3, 4, 5])
result_bytes = my_array.tostring()
import struct
array_of_numbers = struct.unpack('I' * (len(result_bytes) // 4), result_bytes)
print(array_of_numbers)
