#CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE TUDO EM UMA LISTA COMPOSTA. NO FINAL, MOSTRE UM BOLETIM CONTENDO A MÉDIA DE CADA UM E PERMITA QUE O USUÁRIO POSSA MOSTRAR AS NOTAS DE CADA ALUNO INDIVIDUALMENTE (3 NÍVEIS DE LISTA)
import time
aluno=list()
while True:
    aluno.append([str(input('Nome: ')).title(), float(input('Nota 1: ')), float(input('Nota 2: '))])
    inclui=str(input(f'Quer continuar? [S/N] ')).upper()
    if inclui == 'N':
        break
print(f'{"-"*40}')
print(f'{"N°":<5} {"NOME":^10} {"MÉDIA":>10}')
print(f'{"-"*40}')
for i, dados in enumerate(aluno):
    nome=dados[0]
    nota1=dados[1]
    nota2=dados[2]
    media=(nota1+nota2)/2
    print(f'{i:<5} {nome:^10} {media:>10.2f}')
    
while True:
    print(f'{"-"*40}')
    individual=int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if individual == 999:
        time.sleep(1)
        print(f'Finalizando...')
        break
    if individual <0 or individual >=len(aluno):
        print(f'Aluno não encontrado!')
    for i, dados in enumerate(aluno):
        nome=dados[0]
        nota1=dados[1]
        nota2=dados[2]
        if individual == i:
            print("-"*40)
            print(f'{"N°":<5} {"NOME":^10} {"NOTA 1":^10} {"NOTA 2":>10}')
            print(f'{i:<5} {nome:^10} {nota1:^10} {nota2:>10}')
            print("-"*40)
 
 
 
 
 
# CORREÇÃO VIA AULA
# ficha = list()
# while True:
#     nome=str(input('Nome: ')).title()
#     nota1=float(input('Nota 1: '))
#     nota2=float(input('Nota 2: '))
#     media=(nota1+nota2)/2
#     ficha.append([nome, [nota1, nota2], media])
#     resp=str(input('Quer continuar: [S/N] ')).upper()
#     if resp =='N':
#         break
        
# # print(ficha)
# print('-'*26)
# print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
# print('-'*26)
# for i, a in enumerate(ficha):
#     print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
# while True:
#     print('-'*35)
#     opc=int(input('Mostrar notas de qual aluno? (999 interrompe): '))
#     if opc ==999:
#         print(f'Finalizando..')
#         break
#     if opc <=len(ficha)-1:
#         print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')