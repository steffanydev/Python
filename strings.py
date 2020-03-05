frase = 'Aprendendo Python'
# Pega os caracteres do indice 11 a 14
print(frase[11:14])
# Omitindo o segunda parâmetro vai até o fim
print(frase[11:])
# Omitindo o primeiro parâmetro vai desde o início
print(frase[:10])
# Pegando desde o primeiro até o 10 pulando de 2 em 2
print(frase[0:10:2])
# Descobrir o tamanho da String
print(f'A frase tem {len(frase)} posições')
# Descobrir quantas vezes aparece a Letra P
print(f'A letra P aparece {frase.lower().count("p")} vezes')

print('Quantidade de letras d de 0-10: ', frase.count('d', 0, 10), 'letras')
print('Quantidade que aparece Python:', frase.count('Python'), 'vezes')
print('Frase em minuscula:', frase.lower())
print('Frase em maiscula:', frase.upper())
print('Frase Capitalizada:', frase.capitalize())
# Title define todas as primeiras letras em maisculo
print('Primeira letra da palavra:', frase.title())

# Verificar se existe Python na frase
print('Tem Python ?', ('Python' in frase))
# Substituir valor
print(frase.replace('Python', 'corte e custura').title())

# Remove os espaços externos
print('Quantas letras:', len(frase.strip()))
# Remove o espaço do lado esquerdo
print('Quantas letras:', len(frase.lstrip()))
# Remove o espaço do lado direito
print('Quantas letras:', len(frase.rstrip()))
# Remove o espaço do meio da String
print('Quantas letras: ', len(frase.replace(" ", "")))
