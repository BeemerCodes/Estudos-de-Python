print('-=-'*25)

from datetime import date
atual = date.today().year
num = int(input('Qual ano de nascimento? '))
idade = atual - num

if idade <= 9:
    print('Nadador Classe MIRIN!')

elif idade > 9 and idade <= 14:
    print('Nadador Classe INFANTIL!')

elif idade > 14 and idade <= 19:
    print('Nadador Classe JUNIOR!')
    
elif idade > 19 and idade <= 25:
    print('Nadador Classe Sẽnior!')

elif idade > 25:
    print('Nadador Classe MASTER!!')

print('-=-'*25)
