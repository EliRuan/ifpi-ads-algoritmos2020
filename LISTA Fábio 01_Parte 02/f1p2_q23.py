#entrada
valor_mercadoria = float(input('Digite o valor da mercadoria: R$ '))

#processamento
parcelas = float(valor_mercadoria // 3)
entrada = float((valor_mercadoria // 3) + (valor_mercadoria % 3))

#saída
if entrada == parcelas:
    print(f'O valor da entrada e das duas parcelas é R$ {entrada:.2f}')
elif entrada != parcelas:
    print(f'O valor da entrada é R$ {entrada:.2f} e das duas parcelas é R$ {parcelas:.2f} cada.')