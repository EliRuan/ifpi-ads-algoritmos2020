print('-' * 60)
print('Para a expressão: S = (1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50): ')
print('-' * 60)

contador = 1
numerador = 1
soma = 0
print('O valor de S é ', end= '')

while contador <= 50 and numerador <= 99:
    soma = soma + (numerador/contador)
    
    contador += 1
    numerador = numerador + 2

print(f'{soma:.2f}')
