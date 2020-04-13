Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = float(input('Digite o valor que quer obter desconto: '))
d = int(input('Digite quanto é o valor do desconto: '))
print('===Com desconto de {}% aplicado voce pagara: R${}==='.format(d, n-(n*d/100)))
