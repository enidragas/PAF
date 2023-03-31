import math

tocke= [5,6,7,9,4,3,1,2,6,1]
print('Brojevi:', tocke)
suma = 0 
for x in tocke:
    suma += x;

arS= suma/10

print('Aritmetička sredina 10 brojeva:', arS)

suma2= 0

for y in tocke:
    suma2 += pow(y-arS, 2)

stD= math.sqrt(suma2/9)

print('standardna devijacija:', stD)

