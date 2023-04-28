import numpy as np
import math 
import matplotlib.pyplot as plt
from scipy.integrate import quad

def kvadrat(x):
	return round(x*x)

def kub(x):
	return x*x*x

def derivacija_u_tocki(x,arg):
    h = 1e-5
    return (arg(x+h)-arg(x-h))/(2*h)
    

def deriv(x_donja,x_gornja, h,arg):
    
    n = int(abs(x_gornja-x_donja)/h) # broj tocaka
    xs = np.linspace(start=x_donja, stop=x_gornja, num=n) # x values
    y = np.array([arg(i) for i in xs]) # nasa funkcija


    d = np.zeros_like(y)
    for i in range(1, y.shape[0]-1):
        d[i] = (y[i+1] - y[i-1])/(2*h)
        return xs,y,d

def get_numerical_info(data):
	if data.lower()=="x":
		print("polje x: ",x)
	elif data.lower()=="y":
		print("polje y:",y)
	elif data.lower()=="y1":
		print("polje y1:",y1)
	 
	

def plot_derivacija():
	plt.plot(x,y,"-",label="Function",color="blue") 
	plt.plot(x,y1,"-",label="Derivative",color="red")
	plt.legend(fontsize=10)
	plt.show()
	return 

h = 0.01 # step size
x,y,y1 = deriv(0,5,h,math.sin) # first derivative

x = x[1:]
x=x[:-1]
y= y[1:]
y=y[:-1]
y1=y1[1:]
y1=y1[:-1]




