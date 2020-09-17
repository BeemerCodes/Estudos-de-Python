print('{:=^46}'.format(' LOLJA '))

preco = float(input('Total Das Compras: R$'))
print('''Formas De Pagamento
[ 1 ] á Vista Dinheiro/Cheque
[ 2 ] á vista Cartão
[ 3 ] 2x No Cartão
[ 4 ] 3x Ou Mais No Cartão''')
opção = int(input('Qual opção? '))

if opção == 1:
    total = preco - (preco * 10 / 100)

elif opção == 2:
    total = preco - (preco * 5 / 100)

elif opção == 3:
    total = preco
    parcela = total / 2
    
    print('Sua compra sera parcelada em  2x de R${}'.format(parcela))
     
elif opção == 4:
    
     total = preco + (preco * 20 / 100)
     
     vzs = int(input('Quantas parcelas? '))
     
     parcela = total / vzs
     
     print('Sua compra será parcelada em  {}x de R${:.2f}'.format(vzs, parcela))
    
else:
    total = 0
    preco = 0
    print('Selecione outra opção :(')
    
print('Sua compra de  R${:.2f} vai custar R${:.2f} no final'.format(preco, total))

    
