nome = str(input('Qual é seu nome? '))
if nome == 'pedro':
    print ('Que nome bonito!')
elif nome == 'joão' or nome == 'maria' or nome == 'paulo':
    print('Seu nome é muito popular no brasil !!')
else:
    print('Que nome sem graça!')
     
print('tenha um ótimo dia, {}!'.format(nome))
