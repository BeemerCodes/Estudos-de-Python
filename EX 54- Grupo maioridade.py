print('='*30)
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for idade in range(1, 8):
    num = int(input('Em que ano a {}°pessoa nasceu? '.format(idade)))
    idade = atual - num
    if idade > 21:
        maior += 1
    else:
        menor += 1
print('O total de maiores de idade são {}'.format(maior))
print('O total de menores de idade são {}'.format(menor))
print('='*25)
