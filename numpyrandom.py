#write a numpy program to create random array with 1000 elements and find mean,var,std dev
import numpy as np
x=np.random.randn(1000)
print(x)
print("Average")
print(x.mean())
print("Standard deviation:")
print(x.std)
print("Variance:")
print(x.var())
