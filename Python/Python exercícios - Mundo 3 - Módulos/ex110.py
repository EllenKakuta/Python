#ADICIONE AO MÓDULO moeda.py CRIADO NOS DESAFIOS ANTERIORES UMA FUNÇÃO CHAMADA resumo(), QUE MOSTRE NA TELA ALGUMAS INFORMAÇÕES GERADAS PELAS FUNÇÕES QUE JÁ TEMOS NO MÓDULO CRIADO ATÉ AQUI
'''
p=float(input('Digite o preço: ))
moeda.resumo(p,80,35)
------------------------------
       RESUMO DO VALOR
------------------------------
Preço analisado:     R$500,00
Dobro do preço:      R$1000,00 
Metade do preço:     R$250,00
80% de aumento:      R$900,00
35% de redução:      R$325,00
------------------------------

'''
import moeda
p=float(input('Digite o preço: R$'))
moeda.resumo(p,80,35)