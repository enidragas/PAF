import numpy as np
import matplotlib.pyplot as plt

x = [0.1745,0.3491,0.5236,0.6981,0.8727, 1.0472]
y = [0.052,0.124,0.168,0.236,0.284,0.336]

z = 0
kut_2 = []

for i in range(6):
    z += y[i]*x[i]
    kut_2.append(x[i]**2)

sK = np.sum(kut_2) / 6
a = (z/6) / sK

podaci = []

for i in range (6):
    podaci.append(x[i]*a)

plt.scatter(x,y, color= 'red')
plt.xlabel('phi[rad]')
plt.ylabel('M [N/m]')
plt.plot(x, podaci)
plt.show()



