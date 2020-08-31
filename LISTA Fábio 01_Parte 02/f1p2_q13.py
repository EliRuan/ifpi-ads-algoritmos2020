#entrada
ano = int(input('Digite um valor em anos: '))
meses = int(input('Digite um valor em meses: '))
dias = int(input('Digite um valor em dias: '))

#processamento
n_total_dias = (ano * 365) + (meses * 30) + dias

#saída
print('O total de dias é:', n_total_dias)
