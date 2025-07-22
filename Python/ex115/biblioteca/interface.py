def leiaInt(n):
    while True:
        try:
            num=int(input(n))               
        except (ValueError,TypeError):
            print(f'\033[31mERRO: por favor digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mO usuário preferiu não informar os dados\033[m')
            return 0
        else:
            return num

def linha(tamanho=40):
    return '-'* tamanho

def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opcao= leiaInt('Sua opção: ')
    return opcao
    




#MINHA RESOLUÇÃO, ESTAVA EXTENSO PORÉM OK, MAS A PARTE FINAL DA FORMATAÇÃO NA LEITURA EU NÃO TINHA CONSEGUIDO   
# def c_inicial():
#     with open('dados.txt','w') as arquivo:
#         print('-'*40)
#         print(f'{"NOVO CADASTRO":^40}')
#         print('-'*40)
#         nome=input('Nome: ')
#         idade=input('Idade: ')
#         arquivo.write(f'{nome};{idade}')
#         print(f'Novo cadastro de {nome} adicionado.')

# def cadastrar():
#     with open('dados.txt','a') as arquivo:
#         print('-'*40)
#         print(f'{"NOVO CADASTRO":^40}')
#         print('-'*40)
#         nome=(input('Nome: '))
#         idade=(input('Idade: '))
#         arquivo.write(f'{nome};{idade}')
#         print(f'Novo registro de {nome} adicionado.')

# def listar():
#     with open('dados.txt','r') as arquivo:
#         # conteudo=arquivo.read()
#         print('-'*40)
#         print(f'{"PESSOAS CADASTRADAS":^40}')
#         print('-'*40)
#         for linha in arquivo:
#             print(f'{linha.strip()}')


       