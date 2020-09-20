def programa():
    A = int(input('Valor inicial (A): '))
    R = int(input('Razão da PG: '))
    limite = int(input('Limite da PG: '))

    while A <= limite:
        print(f'{A} → ', end='')
        A *= R
         
    print('FIM')


programa()