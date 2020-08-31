#entrada

x1 = int(input('Digite o valor de x1: '))

y1 = int(input('Digite o valor de y1: '))

x2 = int(input('Digite o valor de x2: '))

y2 = int(input('Digite o valor de y2: '))

#processamento
eixo_x = (x2 - x1) ** 2
eixo_y = (y2 - y1) ** 2

distancia = int(eixo_x + eixo_y) ** 0.5

#saída
print(f'A distância entre o ponto1 ({x1},{y1}) e o ponto2 ({x2},{y2}) é {distancia:.2f}')