print('#'*25)

peso = float(input('Qual é seu peso? '))
altu = float(input('Qual a sua altura? '))
imc = peso / (altu ** 2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso ideal!')

elif imc > 18.5 and imc < 25:
    print('Peso ideal!')

elif imc > 25 and imc < 30:
    print('Sobre peso!')

elif imc > 30 and imc < 40:
    print('Obesidade!!')

else:
    print('Obesidade Mórbida!!!')

print('#'*25)    
