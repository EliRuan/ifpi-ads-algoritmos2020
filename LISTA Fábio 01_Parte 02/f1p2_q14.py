#entrada
n_dias = int(input('Digite um valor para idade em dias: '))

#processamento
anos = int(n_dias / 365)
meses = int((n_dias % 365) / 30)
dias = int((n_dias % 365) % 30)

#saída
print(f'{n_dias} dias correspondem à {anos} ano(s), {meses} mes(es) e {dias} dia(s).')