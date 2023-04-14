import math
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, phi, x0, y0):
        self.v0 = v0
        self.phi = math.radians(phi)
        self.x0 = x0
        self.y0 = y0
        self.reset()

    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * math.cos(self.phi)
        self.vy = self.v0 * math.sin(self.phi)
        self.t = 0

    def __move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt - 0.5 * 9.81 * dt**2
        self.vx = self.vx
        self.vy = self.vy - 9.81 * dt
        self.t += dt
    
    def range(self, dt):
        self.reset()
        while (self.y >= 0):
            self.__move(dt)
        return self.x

v0 = 10 
phi = math.radians(60) 
analitičko = (v0**2 * math.sin(2*phi)) / 9.81

lista = [0.01,1, 10]   #dt

rel_pogr = []
for dt in lista:
    p = Particle(v0, 60, 0, 0)
    numeričko = p.range(dt)
    relativnagreska = abs(numeričko - analitičko) / analitičko* 100
    rel_pogr.append(relativnagreska)

plt.plot(lista, rel_pogr)
plt.xscale('log')
plt.xlabel('dt')
plt.ylabel('Relativna pogreška')
plt.show()

                  

