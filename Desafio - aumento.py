n = float(input('Qual é o salario: '))
a = int(input('Qual a porcentagem de aumento? '))
print('O novo salario será de: R${:.2f}'.format(n+(n*a/100)))
