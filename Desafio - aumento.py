Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = float(input('Qual é o salario: '))
a = int(input('Qual a porcentagem de aumento? '))
print('O novo salario será de: R${:.2f}'.format(n+(n*a/100)))
