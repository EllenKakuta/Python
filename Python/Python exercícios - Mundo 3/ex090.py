#FAÇA UM PROGRAMA QUE LEIA NOME E MÉDIA DE UM ALUNO, GUARDANDO TAMBÉM A SITUAÇÃO EM UM DICIONÁRIO. NO FINAL, MOSTRE O CONTEÚDO DA ESTRUTURA NA TELA
#Nome:Joaquim
#Média: 4.5
#Nome é igual a Joaquim
#Média é igual a 4.5
#Situação é igual a Reprovado

aluno={}
aluno['nome']=str(input('Nome: ')).title()
aluno['media']=float(input('Média: '))
if aluno['media']>=7:
    aluno['situacao']='Aprovado'
elif aluno['media'] <=5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao']='Reprovado'
print('-'*40)
# print(f'Nome é igual a {aluno["nome"]}')
# print(f'Média é igual a {aluno["media"]}')
# print(f'Situação é igual a {aluno["situacao"]}')
# print('-'*40)

for k,v in aluno.items():
    print(f' - {k} é igual a {v}')