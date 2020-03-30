preco = float(input('Informe o valor do produto R$ '))
print('Qual será a forma de pagamento? \n 1 - À vista dinheiro | cheque \n 2 - À vista no cartão \n 3 - Em até 2x no cartão \n 4 - 3x ou mais no cartão')
formapag = int(input('Digite a forma de pagamento: '))

# 1 - À vista dinheiro | cheque: 10% desconto
if formapag == 1:
    valor = preco - (preco * (10/100))
# 2 - À vista no cartão: 5% de desconto
elif formapag == 2:
    valor = preco - (preco * (5/100))
# 3 - Em até 2x no cartão: preço normal
elif formapag == 3:
    valor = preco
    parcela = valor / 2
    print('\n Seu produto em 2x no cartão a parcela custará R${:.2f}'.format(parcela))
# 4 - 3x ou mais no cartão: 20% de juros
elif formapag ==4:
    valor = preco + (preco * (20/100))
    quanpar = int(input('Será em quantas parcelas?'))
    parcela = valor / quanpar
    print('\n Seu produto em {}x no cartão a parcela custará R${:.2f} + Juros de 20%'.format(quanpar, parcela))

# Mostrando o valor
print('\n O produto custará R${:.2f}'.format(valor))

