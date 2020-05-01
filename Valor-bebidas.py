porcao = 0
valor = 0
energetico = 0
gelo = 0
tot1 = 0
totalg = 0
print("[1]Chanceler  [2]Passaporte")
tipowhisky = int(input("Qual o Whisky? "))
quantidade = float(input("Quantos litros são de whisky? "))
if tipowhisky == 1:
    valor = 15
else:
    valor = 40
if valor == 15:
    porcao = 6
else:
    porcao = 10
if porcao == 6:
    energetico = 2400
else:
    energetico = 4000
if energetico == 2400:
    gelo = 12
else:
    gelo = 20
tot1 = valor + gelo
if porcao == 6:
    totalg = 6
else:
    totalg = 10

print("Sera usado {} Gelos de coco ou maracujá.".format(int (totalg * quantidade)))
print("Sera usado {}L de whisky!".format(quantidade))
print("Sera usado {}L de energetico!".format(energetico))
print("Serão feitas {} porções de bebida!".format(int (porcao * quantidade)))
print("O valor total sera de R${:.2f}".format(tot1 * quantidade))
