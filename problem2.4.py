import math
x = input("Enter distance in light")
v = input("Enter speed as a fraction of speed of light")
x = float(x)
v = float(v)
t = (x/v)
u = t * math.sqrt(1 -(v*v))
print("Time measured on earth in years", t)
print("Time measured on spaceship in years", u)
