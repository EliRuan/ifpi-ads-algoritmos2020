#entrada
custo_de_fabrica = float(input('Digite o custo de fábrica do carro: R$ '))

#processamento
distrib = float(48/100 * custo_de_fabrica)

impostos = float(45/100 * custo_de_fabrica)

custo_consumidor = float(custo_de_fabrica + distrib + impostos)

#saída
print(f'O preço do carro para o consumidor é: R$ {custo_consumidor:.2f}')