from random import shuffle
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
a5 = str(input('Aluno 5: '))
lista = [a1, a2, a3, a4, a5]
shuffle(lista)
print('A ordem de apresentação será: {}')
print(lista)
