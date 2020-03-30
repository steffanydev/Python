from random import randint
# Jogo Pedra, Papel e Tesoura
objetos = ('Pedra', 'Papel', 'Tesoura')
numero = randint(0,2)
print('')
print('Escolha uma opção:')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('')
jogador = int(input('Digite sua opção: '))

# Pedra
if numero == 0:
    # Pedra
    if jogador == 0:
        print('EMPATE')
    # Papel
    elif jogador == 1:
        print('VITÓRIA - JOGADOR')
    # Tesoura
    elif jogador == 2:
        print('VITÓRIA - COMPUTADOR')
# Papel
elif numero == 1:
    # Pedra
    if jogador == 0:
        print('VITÓRIA - COMPUTADOR')
    # Papel
    elif jogador == 1:
        print('EMPATE')
    # Tesoura
    elif jogador == 2:
        print('VITÓRIA - JOGADOR')
# Tesoura
elif numero == 2:
    # Pedra
    if jogador == 0:
        print('VITÓRIA - JOGADOR')
    # Papel
    elif jogador == 1:
        print('VITÓRIA - COMPUTADOR')
    # Tesoura
    elif jogador == 2:
        print('EMPATE')

print('')
print('O computador escolheu {}.'.format(objetos[numero]))
print('O computador escolheu {}.'.format(objetos[jogador]))

