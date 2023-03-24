import numpy as np
import matplotlib.pyplot as plt

def funkcija(F, m, x0, v0, tmax, dt):
    N= int(tmax/ dt) + 1 #broj koraka

    x= np.zeros(N)
    v= np.zeros(N)
    a= np.zeros(N)

    x[0]= x0
    v[0]= v0

    a[0]= F/m

    for i in range(1, N):
        x[i]= x[i-1] + v[i-1]* dt
        v[i]= v[i-1] + a[i-1]* dt
        a[i]= F/m

    t= np.linspace(0, tmax, N)

    plt.subplot(3,1,1)
    plt.plot(t,x)
    plt.ylabel( 'x [m]')
    plt.subplot(3,1,2)
    plt.plot(t,a )
    plt.ylabel('a [m/s**2]')
    plt.xlabel('t [s]')
    plt.subplot(3,1,3)
    plt.plot(t,v)
    plt.ylabel( ' v [m/s]')
    

    plt.show()


F= float(input('unesi silu:'))
m= float(input('unesi masu:'))
x0= 0 #poč pozicija
v0= 0 #poč brzina
tmax= 10 #gibanje prvih 10s
dt= 0.01 

funkcija(F,m, x0, v0, tmax, dt)

    


