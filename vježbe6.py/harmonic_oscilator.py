import numpy as np
import matplotlib.pyplot as plt

class harmonijski_oscilator:
    def __init__(self, x0, v0, k, m ):
        self.x0= x0 #poč. položaj
        self.v0= v0 #poč. brzina
        self.k= k #koeficijent elastičnosti
        self.m= m #masa

    def položaj(self, t):
        omega= np.sqrt(self.k/self.m)
        x= self.x0* np.cos(omega*t)+ (self.v0/omega)* np.sin(omega*t)
        return x
    
    def brzina(self, t):
        omega= np.sqrt(self.k/self.m)
        v= self.x0* omega* np.sin(omega*t)+ self.v0* np.cos(omega*t)
        return v
    
    def akceleracija(self,t):
        omega= np.sqrt(self.k/self.m)
        a= self.k* self.položaj(t)/ self.m
        return a
    
    def HARMONIJSKI_OSCILATOR(self, tmax, dt):
        t= np.arange(0, tmax, dt)
        x= [self.položaj(i) for i in t]
        plt.subplot(1,3,1)
        plt.title('x-t graf')
        plt.plot(t,x)
        plt.xlabel('t[s]')
        plt.ylabel('x [m]')
        

        v= [self.brzina(i) for i in t]
        plt.subplot(1,3,2)
        plt.title('v-t graf')
        plt.plot( t,v)
        plt.xlabel( 't [s]')
        plt.ylabel(' v [m/s]')
        

        a= [self.akceleracija(i) for i in t]
        plt.subplot(1,3,3)
        plt.title('a-t graf')
        plt.plot( t,a)
        plt.xlabel( 't [s]')
        plt.ylabel(' a [m/s^2]')
        plt.show()





        


