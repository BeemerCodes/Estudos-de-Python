nove = ''
idve = 0
contm = 0
somaidade = 0
for cont in range(1, 6):
    print('------------ {}° Pessoa ------------'.format(cont))
    nome = str(input('Qual é seu nome: ')).upper().strip()
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Maculino [M] Feminino [F]: ')).strip().upper()
    somaidade += idade
    if cont == 1 and sexo in 'Mm':
        idve = idade
        nove = nome
    if sexo in 'Mm' and idade > idve:
        idve = idade
        nove = nome
    if sexo in 'Ff' and idade < 20:
        contm += 1
media = somaidade / 4
print('-'*35)
print('A média de idade das pessoas do seu grupo é de {}'.format(media))
print('O homem mais velho do grupo é {} com {} anos'.format(nove, idve))
print('O total de mulheres nesse grupo com menos de 20 anos é {}'.format(contm))
print('-'*35)


    
