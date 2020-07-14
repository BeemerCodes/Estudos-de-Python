print('=-='*20)

casa = float(input('Qual valor da casa? R$:'))
sala = float(input('Qual valor do seu salario? R$:'))
time = int(input('Quantos anos deseja pagar? '))

prest = casa / (time * 12)
porc = 30 * sala / 100

if porc >= prest:
    print('Emprestimo aprovado!')
    print('Seu valor disponível para uso é de {}'.format(porc))

elif porc <= prest:
    print('Emprestimo negado!')
    print('Você só pode dispor de {}'.format(porc))
    
print('Para pagar uma casa de {:.2f} em {} anos'.format(casa, time))
print('a prestação sera de R$:{:.2f}'.format(prest))

print('=-='*20)

