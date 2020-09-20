def programa():
    A = int(input('Valor inicial (A): '))
    R = int(input('Razão da PA: '))
    limite = int(input('Limite da PA: '))

    while A <= limite:
        print(f'{A} → ', end='')
        A += R
         
    print('FIM')


programa()
