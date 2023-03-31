def iteracija(N):
    broj1= 5
    for i in range(N):
        broj1 += 1/3
    for j in range(N):
        broj1 -= 1/3
    print('Rezultat',broj1)


print('200')
iteracija(200)
print('2000')
iteracija(2000)
print('20000')
iteracija(20000)
