from array import array
my_array = array('i', [1, 2, 3, 4, 5])
buffer_info = my_array.buffer_info()
print("Địa chỉ bắt đầu của bộ đệm:", buffer_info[0])
print("Số lượng phần tử trong mảng:", buffer_info[1])
