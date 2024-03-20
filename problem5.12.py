import numpy as np
import math

c=2.998e8
hc= 6.63e-34/(math.pi*4)
k= 1.380649e-23

num=math.pow(k,4)
den=4*math.pi*math.pi*hc*hc*hc*c*c
const=num/den
def func(x):
    return math.pow(x, 3)/(math.exp(x)-1)
x1=0.0
x2=20.0
N=100
h=(x2-x1)/N
yarr=np.zeros(N)
sum=0.0
for i in range(1,N):
    yarr[i]=func(x1+h*i)
    sum+=yarr[i]
sum=sum*h*const
print("Stefan's constant is {:.2e}".format(sum))  
   