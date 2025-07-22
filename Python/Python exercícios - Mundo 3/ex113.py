#REESCREVA A FUNÇÃO leiaInt() QUE FIZEMOS NO DESAFIO 104, INCLUINDO AGORA A POSSIBILIDADE DA DIGITAÇÃO DE UM TIPO INVÁLIDO. APROVEITE E CRIE TAMBÉM UMA FUNÇÃO leiaFloat() COM A MESMA FUNCIONALIDADE - Digite um número inteiro: | Digite um número real: | O valor digitado....

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


def leiaFloat(n):
    while True:
        try:
            num=float(input(n))         
        except KeyboardInterrupt:
            print(f'\033[31mO usuário preferiu não informar os dados\033[m')
            return 0
        except ValueError:
            print(f'\033[31mERRO: por favor digite um número real válido\033[m')
            continue
        else:
            return num

n=leiaInt('Digite um número: ')
f=leiaFloat('Digite um número real: ')
print(f'Os valores digitados foram:\n-> número inteiro: {n}\n-> número real: {f}')