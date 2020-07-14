n = float(input('Digite o valor que quer obter desconto: '))
d = int(input('Digite quanto é o valor do desconto: '))
print('===Com desconto de {}% aplicado voce pagara: R${}==='.format(d, n-(n*d/100)))
