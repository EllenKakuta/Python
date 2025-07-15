#MODIFIQUE AS FUNÇÕES QUE FORAM CRIADAS NO DESAFIO 107 PARA QUE ELAS ACEITEM UM PARÂMETRO A MAIS, INFORMANDO SE O VALOR RETORNADO POR ELAS VAI SER OU NAO FORMATADO PELA FUNÇÇÃO moeda(), DESENVOLVIDA NO DESAFIO 108.
'''
EX> cód principal
p=float(input('Digite o preço:))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}) - o True vai dizer se vai ser formatado ou não
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)})
print(f'Aumentando 10%, temos {moeda.aumentar(p,10, True)})
print(f'Diminuindo 13%, temos {moeda.diminuir(p,13, True)})
'''
import moeda

p=float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10,True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p,13,True)}')