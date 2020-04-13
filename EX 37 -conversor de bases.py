num1 = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ]  Converter para Binario
[ 2 ]  Converter para Octal
[ 3 ]  Converter para Hexadecimal ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} Convertido para binario é igual a {}'.format(num1, bin(num1)[2:]))     

elif opção == 2:
    print('{} Convertido para octal é igual a {}'.format(num1 , oct(num1)[2:]))

elif opção == 3:
    print('{} Convertido para Hexadecimal é igual a {}'.format(num1, hex(num1)[2:]))

else:
    print('Opção invalida!')
