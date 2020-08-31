#entrada
n_horas = int(input('Digite um valor em horas: '))

#processamento
n_dias = n_horas // 24
n_semanas = n_dias // 7

#saída
print(f'{n_horas} h correspondem à {n_semanas} semana(s), {n_dias % 7} dia(s) e {n_horas % 24} hora(s).')

