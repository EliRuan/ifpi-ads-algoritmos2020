# entrada

n_anos = int(input("Digite o nº de anos que fuma: "))

n_por_dia = int(input('Digite o nº de cigarros fumados por dia: '))

valor_carteira = float(input('Digite o preço da carteira de cigarro: R$ '))



#processamento

tempo = n_anos * 365

cigarros_por_ano = n_por_dia * tempo

carteiras_por_ano = cigarros_por_ano // 20

total_gasto = float(carteiras_por_ano * valor_carteira)




#saída

print('O total gasto foi: R$', total_gasto)