#entrada
n_minutos = int(input('Digite um valor em minutos: '))

#processamento
n_horas = n_minutos // 60
n_dias = n_horas // 24

#saída
print(f'{n_minutos} min correspondem à {n_dias} dia(s), {n_horas % 24} h e {n_minutos % 60} min.')
