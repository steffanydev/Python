# Crie um sistema que gere a tabuada de um número que o usuário escolher utilizando a estrutura de repetição FOR.
numero = int(input("Informe um número: "))
for tabuada in range(0, 11):
    print('{} X {} = {}'.format(numero, tabuada, numero * tabuada))