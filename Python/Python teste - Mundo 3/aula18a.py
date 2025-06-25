'''
VARIÁVEIS COMPOSTAS- LISTAS(PARTE2)

listas podem ser criadas com [] ou list()
Ex: dados= list() ou dados=[]

dados=list()
dados.append('Pedro')
dados.append(25)
                   0    1
print(dados) -> [Pedro,25]
print(dados[0]) ->Pedro
print(dados[1]) ->25

pessoas=list()
pessoas.append(dados[:]) -fatiamento completo da estrutura de dados, uma cópia
                        0            1         2
print(pessoas) -> ['Pedro' 25, 'Maria' 19, 'João' 32]
               0             1          2
pessoas=[['Pedro',25],['Maria',19],['João',32]]
print(pessoas[0][0]) ->Pedro
print(pessoas[1][1]) ->19
print(pessoas[2][0]) ->João
print(pessoas[1]) ->['Maria',19]
'''

#PARTE PRÁTICA
teste=list()
teste.append('Ellen')
teste.append(40)
galera=list()
galera.append(teste[:])
teste[0]='Maria'
teste[1]=22
galera.append(teste[:])
print(galera)

galera=[['João',19],['Ana',33],['Joaquim',13],['Maria',45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])

for p in galera:
    print(p)
    print(p[0])
    print(p[1])
    print(f'{p[0]} tem {p[1]} anos de idade')

galera=list()
dado=list()
total_maior = total_menor=0
for c in range(0,5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() #apaga os dados cada vez que faz o laço
print(galera)
  
for p in galera:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade')
        total_maior+=1
    else:
        print(f'{p[0]} é menor de idade')
        total_menor+=1
print(f'Temos {total_maior} maiores e {total_menor} menores de idade')