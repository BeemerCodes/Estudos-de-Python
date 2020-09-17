from random import randint
from time import sleep
computador = randint(0, 10) # IA que faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 10, Tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Em que numero pensei? ')) # O jogador escolhe o numero
print('PROCESSANDO...')
sleep(1.5)
if jogador == computador:
    print('Você acertou, Parabens!!')
else:
    print('HAHAHAHA, Ganhei, Eu pensei no numero {} e não {}!'.format(computador, jogador))
