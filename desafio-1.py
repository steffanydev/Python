print('Empresa Tinta Seca')
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
print('Será necessário {:.2f} latas de tintas'.format(area / 2))
