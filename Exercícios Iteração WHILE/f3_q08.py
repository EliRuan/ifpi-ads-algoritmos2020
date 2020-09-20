def programa():
    n = int(input('Número: '))
    lim_inferior = int(input('Limite inferior: '))
    lim_superior = int(input('Limite superior: '))

    while lim_inferior <= lim_superior:
        if lim_inferior % n ==0:
            print(lim_inferior,'→', end=' ')
        lim_inferior += 1
        

    print('Fim')

programa()
