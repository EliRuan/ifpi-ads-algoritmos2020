resposta = 'S'
maior = menor = quant = 0
while resposta in 'Ss':
    n = int(input('Digite um número: '))
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip() [0]

print(f'O maior número é {maior}.')
