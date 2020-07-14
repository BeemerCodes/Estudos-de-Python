n1 = float(input('Quanto foi a Quilometragem rodada?: '))
n2 = int(input('Quantos dias o carro foi utilizado?: '))
print('O total  pagar é: R${:.2f}'.format(n1*0.15+n2*60))
