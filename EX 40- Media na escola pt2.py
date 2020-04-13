num1 = float(input('Primeira nota: '))
num2 = float(input('Segunda nota: '))
resp = (num1 + num2) / 2

if resp > 7.0:
    print('Parabéns! Você foi aprovado com a nota {}'.format(resp))

elif resp > 5.0 and resp < 6.9:
    print('Você esta de recuperação com a nota {}'.format(resp))

else:
    print('Que pena, Você reprovou com nota {}'.format(resp))
    print('Faltaram {} pontos para você ser aprovado!'.format(7 - resp))
