#entrada
n_segundos = int(input('Digite um valor em segundos: '))

#processamento
n_minutos = n_segundos // 60
n_horas = n_minutos // 60

#saída
print(f'{n_segundos} seg correspondem à {n_horas} h, {n_minutos % 60} min e {n_segundos % 60} seg.')
