def primo():
    lim_inf = int(input('digite Limite inferior: '))
    lim_sup = int(input('digite Limite superior: '))

    é_primo = True

    divisor = lim_inf

    while lim_inf <= lim_sup and é_primo:
        if lim_inf % divisor == 0:
            é_primo = False
        divisor += 1

    if é_primo and lim_inf != 1:
        print((lim_inf),' → ', end= ' ')

    print('FIM')

    
primo()
