print('-' * 50)
print('Para a expressão: S = (1/1 - 1/2 + 1/3 -... +/- 1/N): ')
n = int(input('Digite o valor de N: '))

contador = 1
s = 0
print('O valor de S é ', end= '')

while contador <= n:
    if contador % 2 == 0:
        s = s - (1/contador)
    else:
        s = s + (1/contador)

    contador += 1

print(f'{s:.2f}')
