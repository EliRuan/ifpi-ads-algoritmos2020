resposta = 'S'
soma = quant = média = 0

while resposta in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip() [0]

média = soma / quant

print(f'A média é {média}.')
print(f'A soma é {soma}.')
