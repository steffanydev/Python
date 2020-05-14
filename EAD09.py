times = ('São Paulo', 'Santos', 'Palmeiras', 'Corinthians', 'Chapecoense', 'Ponte Preta', 'Botafogo', 'Santo André',
         'Ituano', 'Guarani')
print('')
# A) Os 5 primeiros
print(f'Os 5 primeiros: {times[:5]}')
# B) Os últimos 4 colocados
print(f'Os últimos 4 colocados: {times[-4:]}')
# C) Times em ordem alfabética
print(f'Times em ordem alfabética: {sorted(times)}')
# D) Em que posição está o time da Chapecoense
print(f'Posição está Chapecoense: {times.index("Chapecoense")}')


# D) Correção
solicitacao = input('Informe o time que quer saber a posição: ')
print(f'O time {solicitacao} está na posição {times.index(solicitacao) + 1} do campeonato')