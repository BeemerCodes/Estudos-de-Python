print("-=-"*20)
print("       C a l c u l a d o r a     d e     g o r ó      ")
valorw = float(input("Qual o valor do whisky? "))
litros = int(input("Quantos litros? "))
gelo = 5
valorg = 2
gelot = (litros * gelo)
valorgt = litros * valorg
print("Serão usados", gelot, "gelos")
print("Fará", gelot, "porções!")
print("OBS: Fara {} porções de 200 de whisky".format(gelot))
energv = 8
energ = 1
energt = litros * energ
energvt = energt * energv
print("você precisara de {}L de energetico".format(energt))
valort = (litros * valorw) + valorgt + energvt
print("Terá valor total de", valort)



