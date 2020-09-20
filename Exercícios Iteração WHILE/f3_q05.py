def fatorial():
    numero = int(input('Número: '))
    fatorial = 1

    while numero >= 1:
        fatorial *= numero
        numero -= 1
    print(f'Fatorial é {fatorial}')


fatorial()