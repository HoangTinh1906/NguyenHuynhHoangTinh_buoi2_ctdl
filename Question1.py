array=[1,2,3,4,5] 
def foo(array):
 sum = 0
 product = 1
 for i in array:
    sum += i
 for i in array:
    product *= i
 print("Sum = "+str(sum)+", Product = "+str(product))
 print(array)
foo(array)