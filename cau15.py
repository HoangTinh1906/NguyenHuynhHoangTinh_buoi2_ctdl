from array import array
my_array = array('b', b'Hello')
print("Mảng trước khi nối chuỗi:", my_array)
string_to_add = " World"
my_array.frombytes(string_to_add.encode('utf-8'))
print("Mảng sau khi nối chuỗi:", my_array)
ascii_values = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
result_string = ''.join(chr(value) for value in ascii_values)
print("Chuỗi ký tự tương ứng với giá trị ASCII là:", result_string)