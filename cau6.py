from array import array
my_array = array('i', [1, 2, 3, 4, 5])
elements_to_add = [6, 7, 8, 9, 10]
my_array.fromlist(elements_to_add)
print(my_array)