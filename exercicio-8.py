preco = float(input('Informe o valor do produto: '))
print('O produto custa R$ {:.2f} e com o desconto de 5% é R$ {:.2f}'.format(preco, (preco - (preco * (5/100)))))