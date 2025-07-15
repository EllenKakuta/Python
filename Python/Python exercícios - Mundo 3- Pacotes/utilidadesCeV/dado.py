#DENTRO DO PACOTE utilidadesCeV QUE CRIAMOS NO DESAFIO 111, TEMOS UM MÓDULO CHAMADO DADO. CRIE UMA FUNÇÃO CHAMADA leiaDinheiro() QUE SEJA CAPAZ DE FUNCIONAR COMO A FUNÇÃO INPUT MAS COM UMA VALIDAÇÃO DE DADOS PARA ACEITAR APENAS VALORES QUE SEJAM MONETÁRIOS - ACEITAR VIRGULAS 99,99, PONTO 99.99 E DAR ERRO PARA VAZIO E STRINGS
import time

# def leiaDinheiro(msg):
#     while True:   
#         p=input(msg.replace(',','.'))     
#         if p.count('.')<=1 and p.replace('.','').isnumeric():
#             return float(p)   
#         else:
#             time.sleep(1)
#             print(f'Informe um valor válido')
#             time.sleep(1)

            
#VIA AULDA DE CORREÇÃO
def leiaDinheiro(msg):
    valido=False
    while not valido:
        entrada=str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada=='':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido=True
            return float(entrada)
