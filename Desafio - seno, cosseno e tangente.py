from math import cos,tan,sin,radians
n1 = float(input('Qual anulo: '))
s = sin(radians(n1))
print('O angulo de {} tem o Seno {:.2f}'.format(n1, s))
c = cos(radians(n1))
print('O angulo de {} tem o Cosseno {:.2f}'.format(n1, c))
t = tan(radians(n1))
print('O angulo de {} tem a Tangente {:.2f}'.format(n1, t))
