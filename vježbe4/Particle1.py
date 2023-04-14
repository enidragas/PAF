import math
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, phi, v0, x0, y0):
     self.v0= v0
     self.phi= phi
     self.x0= x0
     self.y0= y0
     self.x= x0
     self.y= y0
     self.vx= v0*math.cos(math.radians(phi))
     self.vy= v0*math.sin(math.radians(phi))
     self.t= 0

    def reset(self):
       self.x= self.x0
       self.y= self.y0
       self.vx= self.v0*math.cos(math.radians(self.phi))
       self.vy= self.v0*math.sin(math.radians(self.phi))

      

    def __move(self, dt):
       self.x= self.x+ self.vx*dt
       self.vy= self.vy - 9.81*dt
       self.y= self.y + self.vy*dt
     

    def range(self):
       self.reset()
       dt= 0.01
       while (self.y[-1] >= 0):
          self.__move(dt)
       return self.x- self.x0
    
    def plot_trajectory(self):
       self.reset()
       dt= 0.01
       lista_x= []
       lista_y= []
       while (self.y >= self.y0):
          lista_x.append(self.x)
          lista_y.append(self.y)
          self.__move(dt)
       plt.plot(lista_x, lista_y)
       plt.xlabel('x [m]')
       plt.ylabel('y [m]')
       plt.show()
         

     


