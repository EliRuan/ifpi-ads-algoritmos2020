print('-' * 50)
print('Para a expressão: S = (1/N + 1/N-1 + 1/N-2 +... N/1): ')
n = int(input('Digite o valor de N: '))

c = 1
soma = 0
print('O valor de S é ', end= '')

while n >= 1:
    soma = soma + c/n
    n = n - 1
    c = c + 1

print(f'{soma:.2f}')
