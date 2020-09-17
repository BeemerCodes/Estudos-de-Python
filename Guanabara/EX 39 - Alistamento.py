from datetime import date
atual = date.today().year

n1 = int(input('Que ano você nasceu? '))
idade = atual - n1
print('Ano de nascimento {}, idade {}'.format(n1, idade))

if idade == 18:
    print('Você deve se alistar!')

elif idade > 18:
    saldo = idade - 18
    print('Voce deveria ter se alistado ha {} anos!'.format(saldo))
    print('Seu alistamento foi no ano de {}'.format(atual - saldo))
    
else:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, faltam {} anos ainda.'.format(saldo))
    print('Você deve se alistar em {}'.format(atual + saldo))
