def main():

    vetor_a = []

    inserir_valores(vetor_a)
    print(f'Vetor A: {vetor_a}')

    inverter_vetor(vetor_a)
    print(f'Vetor B: {vetor_a}')


def inserir_valores(vetor_a):
    qtd = int(input('Quantos valores desejar inserir? '))
    for i in range(qtd):
        valor = int(input('Valor: '))
        vetor_a.append(valor)

def inverter_vetor(vetor_a):
    vetor_a.reverse()


main()