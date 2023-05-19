import zadatak as zad
import numpy as np
import matplotlib.pyplot as plt
import math

dts= [0.1,0.2,0.5]
for i in dts:
    d2= zad.Projectile(0,0,10,45, 0.1,0.1,0.1,0.1, i)
    x,y= d2.Euler()
    plt.scatter(x,y, s=2)
d3= zad.Projectile(0,0,10,45, 0.1,0.1,0.1,0.1,0.01)
x1,y1=d3.Runnge_Kutta()
plt.plot(x1,y1)
plt.show()



