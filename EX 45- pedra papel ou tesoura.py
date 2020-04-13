from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''ESCOLHA UM NUMERO:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('Qual sua jogada? '))

while jogador < 0 or jogador > 2:
    jogador = int(input("Digite novamente: "))

print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PO!!')

print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)

if computador == 0:
   if jogador == 0:
       print('EMPATE')

   elif jogador == 1:
       print('Jogador Ganhou!!!')

   elif jogador == 2:
       print('Computador Ganhou!!!')


elif computador == 1:
      if jogador == 0:
         print('Computador Ganhou!!!')

      elif jogador == 1:
         print('EMPATE')

      elif jogador == 2:
         print('Jogador Ganhou!!!')



elif computador == 2:
     if jogador == 0:
       print('Jogador Ganhou!!!')

     elif jogador == 1:
         print('Computador Ganhou!!!')
  
     elif jogador == 2:
         print('EMPATE')


