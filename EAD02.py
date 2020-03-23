velocidade = float(input('Informe a velocidade do carro: '))

if velocidade > 80:
    print('Você foi multado! O limite é de 80KM/h')
    # Quanto passou do limite. Multa custa R$ 7,00 por KM acima do limite
    multa = (velocidade - 80) * 7
    print('A multa custara R${:.2f}'.format(multa))
else:
    print('Não ultrapasse a velocidade permitida!')
