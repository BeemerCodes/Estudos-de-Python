print('-=-'*20)
sal = float(input('Qual é o salario? R$:'))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:                  
    novo = sal + (sal * 10 /100)
print('Quem ganhava R${} passa a ganhar R${}!'.format(sal, novo))
print('-=-'*20)
