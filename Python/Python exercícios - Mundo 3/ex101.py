#CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO() QUE VAI RECEBER COMO PARÂMETRO O ANO DE NASCIMENTO DE UMA PESSOA, RETORNANDO O VALOR LITERAL INDICANDO SE UMA PESSOA TEM VOTO NEGADO, OPCIONAL OU OBRIGATÓRIO NAS ELEIÇÕES
import datetime
def voto(dado):   
    if idade >=16 and idade<18 or idade >=65:
        dado='voto opcional'
        return dado
    if idade <=64 and idade >=18:
        dado='voto obrigatório'
        return dado
    if idade <16:
        dado='não vota'
        return dado
        

ano=int(input('Em que ano você nasceu? '))
idade=datetime.date.today().year-ano
print(f'Com {idade} anos: {voto(ano)}')



#código via correção 
#utilização do import dentro da função para otimização de uso da memória

# def voto(ano):
#     import datetime
#     atual=datetime.date.today().year
#     idade=atual-ano
#     if idade <16:
#         return f'Com {idade} anos: NÃO VOTA '
#     elif 16<=idade<18 or idade > 65:
#         return f'Com {idade} anos: VOTO OPCIONAL'
#     else:
#         return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    
# ano=int(input('Em que ano você nasceu?  '))
# print(voto(ano))