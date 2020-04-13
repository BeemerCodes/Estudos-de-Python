print('-=-'*20)
dis = float(input('Qual é a distancia: '))
print('-=-'*20)
print('Você esta prestes a viajar {}Km!'.format(dis))
print('-=-'*20)
if dis <= 200:
    preço = dis * 0.50
else:
    preço = dis * 0.45
print('O valor da passagem sera de {:.2f}'.format(preço))
print('-=-'*20)

# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45

