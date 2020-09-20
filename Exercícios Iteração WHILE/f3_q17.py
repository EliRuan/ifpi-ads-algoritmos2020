print('-' * 50)
print('Para a expressão: S = (1/1 + 1/2 + 1/3 +... 1/N): ')
n = int(input('Digite o valor de N: '))

c = 1
soma = 0
print('O valor de S é ', end= '')

while c <= n:
    soma = soma + 1/c
    c = c + 1

print(f'{soma:.2f}')
