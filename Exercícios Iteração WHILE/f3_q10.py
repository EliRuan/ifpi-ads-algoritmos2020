def impar():
    lim_inf = int(input('digite Limite inferior: '))
    lim_sup = int(input('digite Limite superior: '))


    while lim_inf <= lim_sup:
        if lim_inf % 2 != 0:
            print((lim_inf),' → ', end= ' ')

        lim_inf = lim_inf + 1

    print('FIM')

    
impar()
