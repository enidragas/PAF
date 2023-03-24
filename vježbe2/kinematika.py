import math
import matplotlib.pyplot as plt

def jednoliko_gibanje(v0, t,  a= 0):
    x= v0*t + 0.5*a*t**2
    print(f'položaj nakon {t} sek: {x} m')

    e= [i for i in range(t+1)]
    k= [v0*i + 0.5*a*i**2 for i in e]

    plt.plot(e, k)
    plt.xlabel('t (s)')
    plt.ylabel('x (m)')
    plt.title('graf polozaja u vrimenu')
    plt.show()


def kosi_hitac(v0, kut, t, g=9.81):
    v0x= v0* math.cos(math.radians(kut))
    v0y= v0* math.sin(math.radians(kut))

    x= v0x*t
    y= v0y*t- 0.5*g*t**2
    print('polozaj nakon {t} sekundi')

    vrijednost_vrimena = [i for i in range(t+1)]
    x_pozicija= [v0x* i for i in vrijednost_vrimena]
    y_pozicija= [v0y*i - 0.5*g*i**2 for i in vrijednost_vrimena]
    
    plt.plot(x_pozicija, y_pozicija)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('graf polozaja tijela')
    plt.show()





    

