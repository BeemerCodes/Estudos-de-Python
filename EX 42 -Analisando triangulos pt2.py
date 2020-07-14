num1 = float(input('Primeiro lado: '))
num2 = float(input('Segundo lado: '))
num3 = float(input('Terceiro lado: '))

if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print('Os segmentos podem formar um triângulo ', end='')
    if num1 == num2 == num3:
        print('Equilátero')

    elif num1 != num2 and num1 != num3 and num2 != num3:
        print('Escaleno')

    else:
        print('Isosceles')

else:
    print('Os segmentos não formaram um triângulo!')
        
