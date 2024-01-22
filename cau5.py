import array as arr
my_array=arr.array('i',[1,2,3,4,5])
my_array_2=arr.array('i',[6,7,8,9,10])
my_array.extend(my_array_2)
print(my_array)