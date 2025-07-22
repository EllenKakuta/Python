#CRIE UM PEQUENA SISTEMA MODULARIZADO QUE PERMITA CADASTRAR PESSOAS PELO SEU NOME E IDADE EM UM ARQUIVO DE TEXTO SIMPLES.
#O SISTEMA SÓ VAI TER 2 OPÇÕES: CADASTRAR UMA NOVA PESSOA E LISTAR TODAS AS PESSOAS CADASTRADAS
from biblioteca import arquivo, interface


import time

arq='arquivo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)


while True:
    resposta=interface.menu([ 'Cadastrar Nova Pessoa', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta==1:
        interface.cabecalho('NOVO CADASTRO')
        nome=str(input('Nome: '))
        idade=int(input('Idade: '))
        arquivo.cadastrar(arq,nome,idade)
    elif resposta==2:
        arquivo.lerArquivo(arq)
    elif resposta==3:
        time.sleep(1)
        interface.cabecalho('Finalizando o sistema.. Até logo!')
        break
    else:
        print(f'\033[31mERRO: escolha uma opção válida\033[m')
    time.sleep(2)



# while True:  
#     try:
#         cadastro.menu('')
#         n=int(input(f'Sua opção: '))
#         if n==1:
#             if not n:
#                 cadastro.c_inicial()
#             else:
#                 cadastro.cadastrar()
#             cadastro.listar()
#         if n==2:
#             cadastro.listar()
#         if n==3:
#             print(f'Finalizando..')
#             break
#         else:
#             print(f'\033[31mERRO: escolha uma opção válida\033[m')
#     except Exception as erro:
#         print(f'Problema encontrado foi {erro.__cause__}')