metro = float(input('Digite um valor: '))
print('Metros {:.0f}m'.format(metro))
print('Centímetros {:.0f}cm'.format(metro * 100))
print('Milímetros {:.0f}mm'.format(metro * 1000))
print('{:.0f}m equivale a {:.0f}cm e {:.0f}mm'.format(metro, (metro * 100), (metro * 1000)))