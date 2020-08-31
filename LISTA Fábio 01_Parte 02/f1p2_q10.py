#entrada
num1 = input('Digite um número inteiro (3 dígitos): ')

#processamento
inverso_num1 = num1[ : : -1]
soma_n_inverso = int(num1) + int(inverso_num1)

#saída
print(f'A soma entre {num1} e seu inverso é:', soma_n_inverso)