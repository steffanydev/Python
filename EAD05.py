from datetime import date
anonas = int(input('Informe o ano que você nasceu: '))
anoatual = date.today().year
idade = anoatual - anonas

if idade < 18:
    falta = 18 - idade
    print('Você não tem 18 anos. Falta {} anos.'.format(falta))
elif idade == 18:
    print('Você tem que se alistar.')
else:
    passou = idade - 18
    print('Já passou do tempo do alistamento por {} anos'.format(passou))