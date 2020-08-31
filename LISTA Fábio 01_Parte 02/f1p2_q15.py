#entrada
f1 = input('Digite a primeira fração: ')
f2 = input('Digite a segunda fração: ')

#processamento
from fractions import Fraction
soma = Fraction(f1) + Fraction(f2)  

#saída
print('A soma das frações é:', soma)
