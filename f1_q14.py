#entrada
nota_1 = int(input('Digite a primeira nota (peso 1): '))
nota_2 = int(input('Digite a segunda nota (peso 2): '))
nota_3 = int(input('Digite a terceira nota (peso 3): '))

#processamento
média_ponderada = ((nota_1 * 1) + (nota_2 * 2) + (nota_3 * 3)) / 6

#saída
print('A média ponderada das 3 notas é:', média_ponderada)
