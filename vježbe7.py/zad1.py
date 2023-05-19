import zadatak as zad
import numpy as np
import matplotlib.pyplot as plt
import math


d1= zad.Projectile(0,0,10,45, 0.1,0.1,0.1,0.1)
a,b= d1.Euler()
plt.plot(a,b)
plt.show()

