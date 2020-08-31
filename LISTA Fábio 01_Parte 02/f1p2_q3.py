#entrada
q_dias = int(input('Digite um valor em dias: '))

#processamento
semana = q_dias // 7

#saída
print(f'{q_dias} dias correspondem à {semana} semana(s) e {q_dias % 7} dia(s).')