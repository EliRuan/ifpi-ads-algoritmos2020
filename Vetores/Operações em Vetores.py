def main():

    menu = '*** Brincando com Listas ***'
    menu += '\n 1 -  Inserir Valores'
    menu += '\n 2 -  Mostrar Valor (posição)'
    menu += '\n 3 -  Mostrar Valor (todos)'
    menu += '\n 4 -  Remover Valor (posição)'
    menu += '\n 5 -  Atualizar Valor (posição)'
    menu += '\n 6 -  Calcular média (posição)'
    menu += '\n 7 -  Total de nº pares (posição)'
    menu += '\n 8 -  Total de nº ímpares (posição)'
    menu += '\n 9 -  Total de nº positivos (posição)'
    menu += '\n 10 - Total de nº negativos (posição)'
    menu += '\n 11 - Dobrar valores (posição)'
    menu += '\n 12 - Apagar lista (posição)'
    menu += '\n 0 -  Sair '
    menu += '\n Opção >>> '

    lista = []

    while True:
        opcao = int(input(menu))

        if opcao == 1:
            inserir_valores(lista)
        elif opcao == 2:
            mostra_valor(lista)
        elif opcao == 3:
            mostrar_todos(lista)
        elif opcao == 4:
            remover_valor(lista)
        elif opcao == 5:
            atualizar_valor(lista)
        elif opcao == 6:
            calcular_media(lista)
        elif opcao == 7:
            total_pares(lista)
        elif opcao == 8:
            total_impares(lista)
        elif opcao == 9:
            total_positivos(lista)
        elif opcao == 10:
            total_negativos(lista)
        elif opcao == 11:
            dobrar_valores(lista)
        elif opcao == 12:
            apagar_lista(lista)
        elif opcao == 0:
            break
        else:
            print('Opção Inválida')

        input('...aperte ENTER para continuar...')


def inserir_valores(lista):
    qtd = int(input('Quantos valores desejar inserir? '))

    for i in range(qtd):
        valor = int(input('Valor: '))
        lista.append(valor)

    print('Valores inseridos com sucesso!')


def mostra_valor(lista):
    posicao = int(input('Qual posição? '))
    print('Valor buscado:')
    print(f'Valor index[{posicao}] é {lista[posicao]}')


def mostrar_todos(colecao):
    tamanho = len(colecao)
    print(f'**** Mostrando {tamanho} valores ****')
    for valor in colecao:
        print(f'>> {valor}')


def remover_valor(valores):
    posicao = int(input('Qual posição vc quer remover? '))

    removido = valores.pop(posicao)
    print(f'O valor {removido} foi removido da posição {posicao}!')


def atualizar_valor(cesta):
    pos = int(input('Qual posição? '))

    valor = cesta[pos]
    print(f'Na posição {pos} existe atualmente o valor {valor}')

    novo_valor = int(input('Qual o novo valor? '))
    cesta[pos] = novo_valor
    print('Valor atualizado com sucesso!')


def calcular_media(lista):
    soma = 0
    for valor in lista:
        soma += valor
        media = soma / (len(lista))
    print(f'A média dos valores da lista atual é {media} ')

def total_pares(lista):
    qtd = 0
    for n in lista:
        if n % 2 == 0:
            qtd += 1
    print(f'Total de pares: {qtd}')

def total_impares(lista):
    qtd = 0
    for n in lista:
        if n % 2 != 0:
            qtd += 1
    print(f'Total de ímpares: {qtd}')

def total_negativos(lista):
    qtd = 0
    for n in lista:
        if n < 0:
            qtd += 1
    print(f'Total de negativos: {qtd}')

def total_positivos(lista):
    qtd = 0
    for n in lista:
        if n > 0:
            qtd += 1
    print(f'Total de positivos: {qtd}')

def dobrar_valores(lista):
    print(f'O dobro dos valores atuais é:')
    for i in range(len(lista)):
        lista[i] = lista[i] * 2
        print(f'>> {lista[i]}')

def apagar_lista(lista):
    del lista[0:]
    print(f'Lista apagada com sucesso!')


main()
