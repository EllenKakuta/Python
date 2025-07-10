#CRIE UM PROGRAMA QUE TENHA A FUNÇÃO leiaInt(), QUE VAI FUNCIONAR DE FORMA SEMELHANTE A FUNÇÃO INPUT() DO PYTHON, SÓ QUE FAZENDO A VALIDAÇÃO PARA ACEITAR APENAS UM VALOR NÚMERICO.
#EX: n = leiaInt('Digite um número')

def leiaInt(n):
    while True:
        num=input(n)
        if not num.isnumeric():
            print(f'\033[31mERRO! Digite um número inteiro válido\033[m')
        else:
            return int(num)#convrrsão de string para número
     
n=leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')