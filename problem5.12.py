import numpy as np
import matplotlib.pyplot as plt
import math

c=2.998e8
h= 6.63e-34/(math.pi*4)
k= 1.380649e-23
const= math.pow(k,4)/(4*math.pi*math.pi*c*c*h*h*h)

def func(x):
    return math.pow(x, 3)/(math.exp(x)-1)

N=50
M=10
a= np.zeros(N)
b= np.zeros(N)

for i in range(N):
    a[i]= h*i
    b[i]= func(h*i)
    sum+=h[i]
sum =  sum * h * const
print("Sigma is", sum)    