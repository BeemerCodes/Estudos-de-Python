print('-=-'*20)
print('        F O R M A N D O   U M   T R I Â N G U L O ')
print('-=-'*20)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não formam um triângulo!')
    
