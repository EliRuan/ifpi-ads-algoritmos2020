#entrada
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
d = int(input('Digite o valor de d: '))
e = int(input('Digite o valor de e: '))
f = int(input('Digite o valor de f: '))

#processamento
valor_x = int((c*e - b*f) / (a*e - b*d))
valor_y = int((a*f - c*d) / (a*e - b*d))

#saída
print(f'O valor de x é {valor_x} e o valor de y é {valor_y}')