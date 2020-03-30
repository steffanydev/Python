import datetime
dia_a = datetime.datetime.now()
qtd_dia = dia_a.strftime("%j")
falta = datetime.ye - float(qtd_dia)
print('Falta {:.0f} dias para o Ano Novo'.format(falta))