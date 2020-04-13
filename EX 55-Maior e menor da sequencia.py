print('='*35)
maior = 0
menor = 0
for c in range(1, 6):
    peso = int(input('Qual o {}° peso? '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
         
print('O maior peso lido foi {}KG'.format(maior))
print('O menor peso lido foi {}KG'.format(menor))
print('='*35)

