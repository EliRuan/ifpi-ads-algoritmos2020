def maior_quadrado():
    n = int(input('Digite um número: '))

    quadrado = n * n
    atual = 1

    while atual **2 <= n:
        quadrado = atual * atual
        atual = atual + 1

    print(f'O maior quadrado até {n} é {quadrado} (quadrado de {atual-1}).')


maior_quadrado()
