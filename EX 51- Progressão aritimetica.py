primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
dec = primeiro + (10 - 1) * razao
for c in range(primeiro, dec + razao, razao):
        print(c)

