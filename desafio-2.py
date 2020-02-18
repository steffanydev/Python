print('Aluguel de Carro')
km = float(input('Informe a quantidade de KM percorridos: '))
dias = float(input('Informa a quantidade de dias: '))
valor_km = km * 0.15
valor_dia = dias * 60
print('O valor de KM é R$ {:.2f}'.format(valor_km))
print('O valor de dias é R$ {:.2f}'.format(valor_dia))
print('O total a ser pago é R$ {:.2f}'.format(valor_km + valor_dia))