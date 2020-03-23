from random import randint
# Sorteia o número
numero = randint(0,5)
print('')
print('Vou sortear um número de 0 a 5.')
print('')
usuario = int(input('Qual será o número?: '))

if usuario == numero:
    print('Parabéns você acertou!')
else:
    print('Você errou! O número era {}.'.format(numero))