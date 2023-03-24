import matplotlib.pyplot as plt
import numpy as np

g= 9.81
v0 =int(input('početna brzina:'))
kut_otklona = float(input('kut otklona:'))
kut_otklona= np.deg2rad(kut_otklona) 
dt= 0.01
t= np.arange(0, 10, dt)

x0= 0 
y0= 0
vx0= v0* np.cos(kut_otklona)
vy0= v0* np.sin(kut_otklona)

def funkcija(vx, vy):
    ax= 0
    ay= -g
    return ax,ay

x= np.zeros_like(t)
y= np.zeros_like(t)
vx= np.zeros_like(t)
vy= np.zeros_like(t)

x[0]= x0
y[0]= y0
vx[0]= vx0
vy[0]= vy0

for i in range(1, len(t)):
    ax,ay= funkcija(vx[i-1], vy[i-1])
    vx[i]= vx[i-1] + ax* dt
    vy[i]= vy[i-1] + ay* dt
    x[i]= x[i-1] + vx[i]* dt
    y[i]= y[i-1] + vy[i]* dt

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.plot(x,y)
plt.xlabel('x (m)')
plt.ylabel(' y(m)')
plt.title('x-y graf')

plt.subplot(1,3,2)
plt.plot(t,x)
plt.xlabel('x (m)')
plt.ylabel('t (s)')
plt.title('x-t graf')

plt.subplot(1,3,3)
plt.plot(t,y)
plt.xlabel('y (m)')
plt.ylabel(' t (s)')
plt.title(' y-t graf')

plt.tight_layout()
plt.show()

