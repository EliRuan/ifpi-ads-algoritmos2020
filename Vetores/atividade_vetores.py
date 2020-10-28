def main():
    tamanho = int(input('Quantos números? '))

    lista = [-1] * tamanho

    print(lista)

    for posicao in range(tamanho):
        lista[posicao] = int(input(f'Número {posicao}: '))

    print(lista)

    qtd_pares = total_pares(lista)
    qtd_impares = total_impares(lista)
    qtd_negativos = total_negativos(lista)
    qtd_positivos = total_positivos(lista)

    print(f'Total de nº pares: {qtd_pares}')
    print(f'Total de nº ímpares: {qtd_impares}')
    print(f'Total de nº negativos: {qtd_negativos}')
    print(f'Total de nº positivos: {qtd_positivos}')


    lista_alterada = alterar_lista(lista)
    print('Lista alterada')
    print(lista)

    qtd_pares = total_pares(lista_alterada)
    qtd_impares = total_impares(lista_alterada)
    qtd_negativos = total_negativos(lista_alterada)
    qtd_positivos = total_positivos(lista_alterada)

    print(f'Total de nº pares: {qtd_pares}')
    print(f'Total de nº ímpares: {qtd_impares}')
    print(f'Total de nº negativos: {qtd_negativos}')
    print(f'Total de nº positivos: {qtd_positivos}')

    media = calcular_media(lista_alterada)
    print(f'Média dos valores: {media}')


def total_pares(lista):
    qtd = 0
    for n in lista:
        if n % 2 == 0:
            qtd += 1
    return qtd

def total_impares(lista):
    qtd = 0
    for n in lista:
        if n % 2 != 0:
            qtd += 1
    return qtd

def total_negativos(lista):
    qtd = 0
    for n in lista:
        if n < 0:
            qtd += 1
    return qtd

def total_positivos(lista):
    qtd = 0
    for n in lista:
        if n >= 0:
            qtd += 1
    return qtd

def alterar_lista(lista):
    for i in range(len(lista)):
        if lista[i] > 0:
            lista[i] = lista[i] * 2
        else:
            lista[i] = lista[i] / 2

    return lista


def calcular_media(lista):
    soma = 0
    for valor in lista:
        soma += valor
        media = soma / (len(lista))
    return media


main()
