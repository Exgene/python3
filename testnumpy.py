import numpy as np
x=np.array([1,3,5,0,-1,-7,0,5])
print("Original array:",x)
r1=np.sign(x)
r2=np.copy(x)
r2[r2>0]=1
r2[r2<0]=-1
print("Element wise indication of the sign for all elements of the said array:")
print(r1)
print(r2)
