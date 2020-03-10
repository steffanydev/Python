# Utilizando Módulos
# import math
from math import ceil, floor, trunc, factorial
n = float(input('Digite um número: '))
print(f'O valor {n} arredondado para CIMA é {ceil(n)}')
print(f'O valor {n} arredondado para BAIXO é {floor(n)}')
print(f'{n} TRUNCADO é {trunc(n)}')
print(f'{n} FATORIAL {factorial(trunc(n))}!')
print(f'{n} elevado à 2 é {pow(n, 2):.2f}')