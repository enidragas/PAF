import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, x,y,v0, kut, m,dt, A, c, p=1.293):
        self.x= x
        self.y= y
        self.kut=kut
        self.vx= v0* np.cos(self.kut)
        self.vy= v0* np.sin(self.kut)
        self.m= m
        self.p= p
        self.c=c
        self.A= A #površina poprečnog presijeka projektila
        self.g= 9.81
        self.dt= dt
        self.xlista= []
        self.ylista= []

    def Euler(self):
        while self.y>=0:
            ax=-np.sign(self.vx)*((self.p*self.c*self.A)/(2*self.m))*(self.vx)**2
            self.vx= self.vx + ax* self.dt
            self.x= self.x + self.vx* self.dt
            self.xlista.append(self.x)
            ay= -self.g- np.sign(self.vy)*((self.p*self.c*self.A)/(2*self.m))*(self.vy)**2
            self.vy= self.vy + ay* self.dt
            self.y= self.y + self.vy* self.dt
            self.ylista.append(self.y)
        return self.xlista, self.ylista
    
    def Runnge_Kutta(self):
        while self.y>=0:
            k1vx = -np.sign(self.vx) * ((self.p * self.c * self.A) / (2 * self.m)) * (self.vx * self.vx)*self.dt
            k1vy = -self.g - np.sign(self.vy) * ((self.p * self.c * self.A) / (2 * self.m)) * (self.vy * self.vy)*self.dt
            k1x = self.vx*self.dt
            k1y = self.vy*self.dt

            k2vx = -np.sign(self.vx+(k1vx/2)) * ((self.p * self.c * self.A) / (2 * self.m)) * ((self.vx+(k1vx/2))*(self.vx+(k1vx/2)))*self.dt
            k2vy = -self.g - np.sign(self.vy+(k1vy/2)) * ((self.p * self.c * self.A) / (2 * self.m)) * (self.vy+(k1vy/2) * (self.vy+(k1vy/2)))*self.dt
            k2x = (self.vx + (k1vx/2))*self.dt 
            k2y = (self.vy + (k1vy/2)) * self.dt

           
            k3vx = -np.sign(self.vx+(k2vx/2)) * ((self.p * self.c * self.A) / (2 * self.m)) * ((self.vx+(k2vx/2))*(self.vx+(k2vx/2)))*self.dt
            k3vy = -self.g - np.sign(self.vy+(k2vy/2)) * ((self.p * self.c * self.A) / (2 * self.m)) * (self.vy+(k2vy/2)*(self.vy+(k2vy/2)))*self.dt
            k3x = (self.vx+(k2vx/2))*self.dt
            k3y =(self.vy+(k2vy/2))*self.dt 

            k4vx = -np.sign(self.vx+(k3vx/2)) * ((self.p * self.c * self.A) / (2 * self.m)) * (self.vx+(k3vx/2)*(self.vx+(k3vx/2)))*self.dt
            k4vy = -self.g - np.sign(self.vy+(k3vy/2)) * ((self.p * self.c * self.A) / (2 * self.m)) * ((self.vy+(k3vy/2))*(self.vy+(k3vy/2)))*self.dt
            k4x = (self.vx + (k3vx/2)) * self.dt
            k4y = (self.vy + (k3vy/2)) * self.dt
            
            ax = (k1vx + 2 * k2vx + 2 * k3vx + k4vx) / 6
            ay = (k1vy + 2 * k2vy + 2 * k3vy + k4vy) / 6

            
            self.vx = self.vx + ax * self.dt
            self.vy = self.vy + ay * self.dt
            self.x = self.x + self.vx * self.dt
            self.xlista.append(self.x)
            self.y = self.y + self.vy * self.dt
            self.ylista.append(self.y)

        return self.xlista, self.ylista





    

