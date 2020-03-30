nota1 = float(input('Informe uma nota: '))
nota2 = float(input('Informe uma nota: '))
nota3 = float(input('Informe uma nota: '))
media = ((nota1 + nota2 + nota3) / 3)

if media >= 7:
    print('APROVADO')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')