#entrada
numero1 = int(input(' 1º dígito binário: '))
numero2 = int(input(' 2º dígito binário: '))
numero3 = int(input(' 3º dígito binário: '))
numero4 = int(input(' 4º dígito binário: '))

#processamanto
soma = (numero4 * 1) + (numero3 * 2) + (numero2 * 4) + (numero1 * 8)

#saída
print(numero1, numero2, numero3, numero4, 'em base decimal é:', soma)

