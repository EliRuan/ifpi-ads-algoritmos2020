def seq():
    n = int(input('Quantidade de termos: '))
    
    t1 = 1
    c = 2
    print(f'→ {t1}', end='')
    while c <= n:
        t2 = t1 + c
        print(f' → {t2} ', end='')
        t1 = t2
        c = c + 1
    print('→ FIM')


seq()
