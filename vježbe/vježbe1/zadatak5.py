import matplotlib.pyplot as plt
import numpy as np

def jedPravca(P,Q):
    a= Q[1]- P[1]
    b= P[0] - Q[0]
    c= a*(P[0]) + b*(P[1])
    if (b<0):
        print("Jednadzba pravca:", a, "x - ", b, "y =", c, "\n")
    else:
        print("Jednadzba pravca:", a, "x + ", b, "y =", c, "\n")
    xpoints= np.array([P[0], Q[0]])
    ypoints= np.array ([P[1], Q[1]])

    plt.plot(xpoints,ypoints)

    p= input("Zelite li prikazati graf? (y/n)")

    if p== "y":
        plt.show()
    else:
        p=input("želite li spremiti graf u PDF obliku? (y/n)")

        if p== "y":
            ime= input("unesite ime pdf-a:")
            plt.savefig(ime+ ".pdf")

P= [1,2]
Q= [2, -3]
jedPravca(P,Q)