def main():

    vetor = []

    inserir_valores(vetor)
    print(vetor)

    calcular_decimal(vetor)
    calcular_hexadecimal(vetor)

def inserir_valores(vetor):
    qtd = 8
    for i in range(qtd):
        valor = int(input('Valor (0 ou 1): '))
        vetor.append(valor)


def calcular_decimal(vetor):
    soma = (vetor[7] * 1) + (vetor[6] * 2) + (vetor[5] * 4) + (vetor[4] * 8)\
           + (vetor[3] * 16) + (vetor[2] * 32) + (vetor[1] * 64) + (vetor[0] * 128)
    print(f'Decimal: {soma}')


def calcular_hexadecimal(vetor):
    soma1 = (vetor[7] * 1) + (vetor[6] * 2) + (vetor[5] * 4) + (vetor[4] * 8)
    soma2 = (vetor[3] * 1) + (vetor[2] * 2) + (vetor[1] * 4) + (vetor[0] * 8)

    if soma2 == 10:
        soma2 = 'A'
    elif soma2 == 11:
        soma2 = 'B'
    elif soma2 == 12:
        soma2 = 'C'
    elif soma2 == 13:
        soma2 = 'D'
    elif soma2 == 14:
        soma2 = 'E'
    elif soma2 == 15:
        soma2 = 'F'

    if soma1 == 10:
        soma1 = 'A'
    elif soma1 == 11:
        soma1 = 'B'
    elif soma1 == 12:
        soma1 = 'C'
    elif soma1 == 13:
        soma1 = 'D'
    elif soma1 == 14:
        soma1 = 'E'
    elif soma1 == 15:
        soma1 = 'F'

    print(f'Hexadecimal: {soma2}{soma1}')

main()
