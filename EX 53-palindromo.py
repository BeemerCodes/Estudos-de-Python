frase = str(input('Digite uma frase: ')).strip().upper() # .strip() tira os espaços
palavras = frase.split()   # .split() separa em grupos
junto = ''.join(palavras) # .join() junta todas as palavras
inverso = ''
for letra in range(len(junto) - 1, -1, -1): # range(len) acha a ultima letra -1
    inverso += junto[letra]                 # o segudno -1 busca a primeira letra
print(junto, inverso)                       # e o ultimo -1 faz ao inverso
if inverso == junto:
    print('Temos um palindromo!')           # inverso += o junto[da letra]
else:
    print('Não é palindromo!!')
