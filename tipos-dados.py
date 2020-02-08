# Tipos de dados
valor = input('Digite alguma coisa: ')
print('O tipo primitivo desse valor é: ', type(valor))
print()
# Funções de verificação de String
print('Esse texto tem espaços? ', valor.isspace())
print('É número? ', valor.isnumeric())
print('É alfabético? ', valor.isalpha())
print('É alfaúmerico? ', valor.isalnum())
print('Está em maiúscula? ', valor.isupper())
print('Está tudo em minúsculo? ', valor.islower())
print('A primeira letra é maiúscula? ', valor.istitle())

# Parse / Conversão
valor = int(input('Informe um número inteiro: '))
print('Tipo de valor: ', type(valor))
print()
valor = float(input('Informe um valor float: '))
print('Tipo de valor: ', type(valor))
print()
valor = bool(input('Diga TRUE para sim ou FALSE para não: '))
print('Tipo do valor: ', type(valor))
# Interpolação de String
print(f'O valor {valor} é do tipo {type(valor)}')