import numpy as np
import math
import matplotlib.pyplot as plt   #Imports to ensure we use the appropriate modules

k= 8.99e9      #Making note of coulomb's constant
ag=0.01
eps=1e-7

def pot(m,n):   #Here we have our defining function. This ensures everything within the function will execute every time we run it.
    r1=ag*math.sqrt(m*m+n*n)   
    r2=ag*math.sqrt((m-10)*(m-10)+n*n)
    if ((r1<eps) or (r2<eps)):
        return 0.0
    return k*((1.0/r1)-(1.0/r2))   
    
M=50

a= np.zeros((2m+1, 2m+1))   #Array created using zeros
for i in in range(-m, m+1):
    for n in range(-m, m+1):
        a[m +M, n+M]= pot(m,n)

fig, ax = plt.subplots(subplot_kw("projection":"3d"))


plane= np.zeros((2m+1, 2m+1))
plt.plot(a, plane)
plt.show()


  
