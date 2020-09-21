print('-' * 50)
print('Para a expressão: S = (1/N - N-1/2 + 3/N-2 -...+/- N/1): ')
n = int(input('Digite o valor de N: '))

contador = 1
valor = n
s = 0
print('O valor de S é ', end= '')

while contador <= n:
    if contador % 2 == 0:
        s = s - (valor/contador)
    else:
        s = s + (contador/valor)

    valor -= 1
    contador += 1

print(f'{s:.2f}')
