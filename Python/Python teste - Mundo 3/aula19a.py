'''
VARIÁVEIS COMPOSTAS - DICIONÁRIOS
lista:
DADOS=LIST()
DADOS.APPEND('PEDRO')
DADOS.APPEND(25)
PRINT(DADOS[0]) = PEDRO
PRINT(DADOS[1]) = 25

dados
'Pedro'  25
  '0     1

-------------------------------------------------------------------------------------------
dicionários = semelhantes as tuplas e as listas, porém é possível personalizar (dar nomes)

Tuplas ()
Listas []
Dicionários {}

dados=dict() OU
dados={'nome':'Pedro', 'idade': 25}

dados
'Pedro'   25
  nome   idade
print(dados['nome']) = Pedro
print(dados['idade']) = 25
dados['sexo']= 'M' (NÃO PRECISA DE APPEND PARA ADICIONAR)

dados
'Pedro'   25      M
  nome   idade   sexo

deldados['idade'] -> PARA DELETAR
dados
'Pedro'     M
  nome    sexo
---------------------------------------------------------------------------------------------------------

filme={'titulo':'Star Wars',
       'ano': 1977,        
       'diretor': 'George Lucas'
    }

filme
'Star Wars'   1977   'George Lucas'    
  titulo      ano      diretor

print(filme.values()) = 'Star Wars', 1977, 'George Lucas'
print(filme.keys())= 'titulo', 'ano', 'diretor'
print(filme.items())= 'titulo''Star Wars', 'ano'1977, 'diretor''George Lucas'

for k,v in filme.items():
    print(f'O {k} é {v}')

    = O titulo é Star Wars
    = O ano é 1977
    = O diretor é George Lucas
*fim de laço
------------------------------------------------------------------------------------------------------------

locadora(lista)
'Star Wars'  1977  'George Lucas' | 'Avengers'  2012  'Joss Whedon'  | 'Matrix'  1999   'Wachowski'
  titulo     ano      diretor     |    titulo    ano     diretor     |  titulo    ano     diretor
              0                                    1                                2

print(locadora[0]['ano']) = 1977
print(locadora[2]['titulo]) = Matrix


NÃO TEM ENUMERATE, NO DICIONÁRIO É NECESSÁRIO UTILIZAR O ITEMS
              
'''

#PARTE PRÁTICA

# pessoas={'nome':'Ellen', 'sexo':'F', 'idade':40}
# print(pessoas)
# print(pessoas['nome'])
# print(pessoas['idade'])
# print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

# for k in pessoas.keys():
#     print(k)

# for k in pessoas.values():
#     print(k)

# for k,v in pessoas.items():
#     print(f'{k} é {v}')

# pessoas['nome']='Kakuta'
# del pessoas['sexo']
# pessoas['peso']=94
# print(pessoas)

#-------------------------------------------------------------------------------------


#DICIONÁRIO DENTRO DE UMA LISTA 
brasil=[]
estado1={'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2={'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
#-------------------------------------------------------------------------------------------------------------
estado=dict()
brasil=list()
for c in range (0,3):
    estado['uf']=str(input('Unidade Federativa: '))
    estado['sigla']=str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #copia o conteúdo de dicionário ao invés de [:]
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}')
    for v in e.values():
        print(v, end=' ')
    print()
print(brasil)