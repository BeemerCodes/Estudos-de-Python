from math import hypot
n1 = float(input('Comprimento do Cateto oposto: '))
n2 = float(input('Comprimento do Cateto adjacente: '))
print('A hipotenusa mede: {:.2f}'.format(hypot(n1,n2)))
