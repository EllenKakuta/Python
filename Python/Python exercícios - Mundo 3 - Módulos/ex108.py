#ADAPTE O CÓDIGO DO DESAFIO 107, CRIANDO UMA FUNÇÃO ADICIONAL CHAMADA moeda() QUE CONSIGA MOSTRAR OS VALORES COMO UM VALOR MONETÁRIO FORMATADO

'''
EX> cód principal
p=float(input('Digite o preço:))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))})
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))})
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))})
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(p,13))})
'''
import moeda

p=float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(p,13))}')