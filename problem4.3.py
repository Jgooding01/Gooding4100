import numpy as np
import matplotlib.pyplot as plt
import math

def func (x):
    return x * (x-1)
def deriv(x, delta): 
    return (func (x+ delta)- func(x))/ delta
    
x = 1
d =0.02
print( deriv(x,d))
#a array and b array
a = np.ones(6)
b = np.zeros(6)
a[0]=.04
b[0]= deriv(x, .04)
for i in range(1,6):
    a[i]= a[i-1]* 0.02
    b[i]= deriv(x, a[i])

plt.xlabel("delta")
plt.title("Derivative")
plt.plot(a, b)
plt.show()  
