Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n1 = float(input('Quanto foi a Quilometragem rodada?: '))
n2 = int(input('Quantos dias o carro foi utilizado?: '))
print('O total  pagar é: R${:.2f}'.format(n1*0.15+n2*60))
