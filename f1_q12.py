#entrada
salário_trabalhador = float(input('Digite o valor do salário: R$ '))

#processamento
aumento = 25/100 * salário_trabalhador
novo_salario = salário_trabalhador + aumento

#saída
print('O novo salário com aumento de 25% é: R$', novo_salario)