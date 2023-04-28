import numpy as np

def kub(x):
      return 4*x**2+5

def integral_pravokutnika(a,b,n,args):
      dx= np.abs(b-a)/n
      x= np.linspace(a,b,n)
      y_up= sum(args(x)*dx) - a*dx
      y_dw= sum(args(x)*dx)- b*dx
      return y_up, y_dw

def integral_trapez(a, b, n, args):
      dx= np.abs(b-a)/n
      x= np.linspace(a,b,n)
      sum= 0
      for i in range(1,n):
            sum += args(x[i-1])+args(x[i])
      integral= dx*sum/2
      return integral

print(integral_pravokutnika(0,1,1000, kub))
print(integral_trapez(0,1,1000, kub))





