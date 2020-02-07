nome = input('Digite seu nome: ')
print(nome + ', seja bem-vinda(a)' + '. Boa noite')
# Pula de linha
print()

curso = input('Digite o curso que você faz: ')
# Primeira forma de concatenar valores com sinal de +
print('O curso de ' + curso + ' é bem legal!')
# Segunda forma de concatenar usando a vírgula
print('O curso de', curso, 'é bem legal!'.format(curso))
# Terceira forma de concatenar com {} format
print('O curso de {} é bem legal, {}!'.format(curso, nome))
# Quarta forma de concatenar com format
print(f'O curso de {curso} é legal {nome}!')