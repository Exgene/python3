#write a function that returns the index of the smallest elements in the array
import numpy as np
my_array = []
a=int(input("Size of array:"))
for i in range(a):
    x=int(input("Element:"))
    my_array.append(x)
index=0
for i in range(0,len(my_array)):
    if my_array[i]<my_array[index]:
        index=i
print(index)
