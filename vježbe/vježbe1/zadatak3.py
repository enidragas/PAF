P= [0,0]
Q= [0,0]

i= 0
for i in range(2):
    k= input("unesi koordinatu:")
    while (k.isdigit()== False):
        k=input("unesi koordinatu:")
    P[i]=int(k);

for i in range(2):
    h=input("unesi koordinatu:")
    while (h.isdigit()== False):
        h=input("unesi koordinatu:")
    Q[i]=int(h);

a= Q[1]-P[1]
b= P[0]-Q[0]
c= a*(P[0]) + b*(P[1])

if(b < 0):
    print("jednadzba pravca:", a, "x -", b, "y = ", c, "\n")
else:
    print("jednadzba pravca:", a, "x + ",b, "y =",c, "\n")
 