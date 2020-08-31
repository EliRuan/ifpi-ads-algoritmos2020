#entrada
latao = float(input('Digite a quantidade de latão em Kg: '))

#processamento
cobre = (70/100) * latao
zinco = (30/100) * latao

#saída
print(f'{latao} kg de latão é composto por {cobre:.2f} kg de cobre e {zinco:.2f} kg de zinco.')
