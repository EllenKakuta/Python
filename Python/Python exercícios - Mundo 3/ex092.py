#CRIE UM PROGRAMA QUE LEIA NOME, ANO DE NASCIMENTO E A CARTEIRA DE TRABALHO E CADASTRE-OS (COM IDADE) EM UM DICIONÁRIO. SE POR ACASO A CTPS FOR DIFERENTE DE ZERO, O DICIONÁRIO RECEBERÁ TAMBÉM O ANO DE CONTRATAÇÃO E O SALÁRIO. CALCULE E ACRESCENTE, ALÉM DA IDADE, COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR.
#SE FOR DIFERENTE DE ZERO, PERGUNTAR O ANO DE CONTRATAÇÃO, O SALÁRIO, APOSENTADORIA COM 35 ANOS DE CONTRIBUIÇÃO

import datetime

dados={}
dados['nome']=str(input('Nome: ')).title()
ano_nascimento=int(input('Ano de nascimento: '))
dados['idade']=datetime.date.today().year - ano_nascimento
dados['ctps']=int(input('Número da carteira de trabalho (0 não tem): '))
if dados['ctps'] !=0:
    dados['contratacao']=int(input('Ano da primeira contratação: '))
    dados['salario']=float(input('Salário: R$'))
    dados['aposentadoria']= (dados['contratacao']-ano_nascimento) + 35
print('-'*100)
print(dados)
print('-'*100)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
