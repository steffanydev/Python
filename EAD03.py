numero = int(input('Digite um número: '))
# Resto da divisão por 2
resultado = numero % 2

if resultado == 0:
    print('{} é PAR'.format(numero))
else:
    print('{} é ÍMPAR'.format(numero))