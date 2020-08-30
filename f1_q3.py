#entrada
minutos = int(input('digite um valor em minutos: '))

#processamento
hora =  minutos // 60
minuto_novo = minutos % 60

#saída
print(f'o valor é {hora} horas e {minuto_novo} minutos:')

