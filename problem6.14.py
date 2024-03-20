import numpy as np             #the start of our program has the usual imports to ensure the right packages are used
import matplotlib.pyplot as plt
import math

c=2.998e8                       #line(5-10) lists our constants used 
hc=6.633-34/(2*math.pi)         #(h cross)
v=20.0
w=1e-9
m=9.1e-31
k=1.38e-23

def y1(E):                       #function number 1
    x=w*w*m*E/(2.0*hc*hc)
    return math.tan(math.sqrt(x))

def y2(E):                        #function number 2
    return math.sqrt((v-E)/E)

def y3(E):                        #function number 3
    return 1/y2/(E)

N=100
x=np.linspace(0.5,19.5,N)
a1=np.zeros(N,dtype=float)         #this creates an array with zeros that will display our desired output
a2=np.zeros(N,dtype=float)
a3=np.zeros(N,dtype=float)
for i in range(N):
    a1[i]=y1(x[i])
    a2[i]=y2(x[i])
    a3[i]=y3(x[i])

plt.xlabel("Energy ev")             #this allocates a name to the x axix
plt.xlim(0,20)
plt.ylim(-10,10)
plt.plot(x,a1,color="red")
plt.plot(x,a2,color="blue")#display of even values
plt.plot(x,a3,color="green")#display of odd values
plt.show()




    
        
