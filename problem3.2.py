import numpy as np
import math
import matplotlib.pyplot as plt

x = np.zeros(50)
y = np.zeros(50)

#Deltoid
theta = np.linspace (0, 2 * math.pi, 10)
for i in range (10):
    x[i] = 2 * math.cos (theta[i]) + math.cos(2*theta[i])
    y[i] = 2 * math.sin (theta[i]) - math.sin(2*theta[i])


#Galilean Spiral
theta = np.linspace(0, 10 * math.pi, 50)
for i in range(50):
    x[i]= theta[i] * theta[i] * math.cos(theta[i])
    y[i]= theta[i] * theta[i] * math.sin(theta[i])

#Feys function
theta = np.linspace(0, 24 * math.pi, 50)
for i in range(50):
    r = math.exp(math.cos(theta[i])) - 2* math.cos(4 * theta[i]) + math.pow(math.sin(theta[i]/12.0), 5)
    x[i] = r* math.cos(theta[i])
    y[i] = r* math.sin(theta[i])


plt.plot(x, y,color ='blue')
plt.title("Graph")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

   
    
    