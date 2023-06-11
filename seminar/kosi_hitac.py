import matplotlib.pyplot as plt
import numpy as np

class Particle:
    def __init__(self, m, kut, x0, y0, v0, dt = 0.001):
        self.m = m
        self.kut = kut
        self.x0 = x0
        self.y0 = y0
        self.y = y0
        self.x = x0
        self.v = v0
        self.vx = self.v * np.cos(kut/180 * np.pi)
        self.vy = self.v * np.sin(kut/180 * np.pi)
        self.dt = dt
        self.g = -9.81
        self.lista_t = []
        self.lista_x = []
        self.lista_y = []
        self.lista_vx = []
        self.lista_vy = []

    def reset(self):
        self.m = self.m
        self.kut = self.kut
        self.x = self.x0
        self.y = self.y0
        self.v = self.v
        self.vx = self.v * np.cos(self.kut/180 * np.pi)
        self.vy = self.v * np.sin(self.kut/180 * np.pi)
        self.dt = self.dt
        self.g = -9.81
        self.lista_t = []
        self.lista_x = []
        self.lista_y = []
        self.lista_vx = []
        self.lista_vy = []


    def putanja(self):
        while self.y > 0:
            self.v = np.sqrt(self.vx**2 + self.vy**2)
            self.x = self.x + self.vx * self.dt
            self.lista_x.append(self.x)
            self.vy = self.vy + self.g * self.dt
            self.y = self.y + self.vy * self.dt
            self.lista_vy.append(self.vy)
            self.lista_y.append(self.y)

        plt.plot(self.lista_x, self.lista_y)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.show()

    
    def maksimalna_visina(self):
        self.reset()
        while True:
            self.vy = self.vy + self.g * self.dt
            if self.vy <= 0:
                break
            self.y = self.y + self.vy * self.dt
        print("Maksimalna visina je: ", self.y)

    def domet(self):
        self.reset()
        while self.y > 0:
            self.x = self.x + self.vx * self.dt
            self.lista_x.append(self.x)
            self.vy = self.vy + self.g * self.dt
            self.y = self.y + self.vy * self.dt
            self.lista_vy.append(self.vy)
            self.lista_y.append(self.y)
        print("Domet je: ", self.x)

    def maksimalna_brzina(self):
        self.reset()
        while self.y > 0:
            self.vy = self.vy + self.g * self.dt
            self.y = self.y + self.vy * self.dt
            self.lista_vy.append(self.vy)
            self.lista_y.append(self.y)
            self.x = self.x + self.vx * self.dt
            self.lista_x.append(self.x)
        self.v = np.sqrt(self.vx**2 + self.vy**2)
        print("Maksimalna brzina je: ", self.v)

    def meta(self, xm, ym, r):
        self.reset()
        brojac = 0
        pocetna_udaljenost = np.sqrt(((xm - self.x)**2) + (ym - self.y)**2)
        while self.y > 0:
            self.x = self.x + self.vx * self.dt
            self.lista_x.append(self.x)
            self.vy = self.vy + self.g * self.dt
            self.y = self.y + self.vy * self.dt
            self.lista_vy.append(self.vy)
            self.lista_y.append(self.y)
            udaljenost = np.sqrt(((xm - self.x)**2) + (ym - self.y)**2)
            if udaljenost <= r:
                brojac = 1
                break
            else:
                if udaljenost - r < pocetna_udaljenost:
                    pocetna_udaljenost = udaljenost - r
        if brojac == 1:
            print("Meta je pogođena.")
        else:
            print("Meta nije pogođena, najmanja udaljenost je bila: {} m".format(pocetna_udaljenost))

        velicina = np.linspace(0, 2 * np.pi, 1000)
        velicina_x = xm + r * np.cos(velicina)
        velicina_y = ym + np.sin(velicina)
        plt.plot(velicina_x, velicina_y, label = "meta")
        plt.plot(self.lista_x, self.lista_y, label = "projektil")
        plt.show()
