#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA AREA(), QUE RECEBA AS DIMENSÕES DE UM TERRENO RETANGULAR (LARGURA E COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO. a=cxl

def area(l,c):
    a=c*l
    print(f'A área de {l:.1f} x {c:.1f} é {a:.1f}m²')

largura=float(input(f'Valor da largura (m): '))
comprimento=float(input(f'Valor do comprimento (m): '))
area(largura,comprimento)