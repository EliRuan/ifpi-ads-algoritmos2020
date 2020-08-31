#entrada
n_meses = int(input('Digite um valor em meses: '))

#processamento
n_anos = n_meses // 12

#saída
print(f'{n_meses} meses correspondem à {n_anos} ano(s) e {n_meses % 12} mes(es).')