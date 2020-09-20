n = int(input('Digite um número: '))
c = 2
print(f'Os números inteiros pares entre 1 e {n} são:')
while c <= n:
    c % 2 == 0
    print(c, end=' ') 
    c += 2
