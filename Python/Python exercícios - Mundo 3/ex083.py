#CRIE UM PROGRAMA ONDE O USUÁRIO DIGITE UMA EXPRESSÃO QUALQUER QUE USE PARÊNTESES.SEU APLICATIVO DEVERÁ ANALISAR SE A EXPRESSÃO PASSADA ESTÁ COM OS PARÊNTESES ABERTOS E FECHADOS NA ORDEM CORRETA.

expressao=str(input(f'Digite uma expressão: '))
contador=0
valida=True
for letra in expressao:
    if "(" in letra:
        contador+=1
    elif ")" in letra:
        contador-=1
    if contador<0:
        valida=False
        break
if contador==0 and valida:
    print(f'Expressão válida')
else:
    print(f'Expressão inválida')


#CORREÇÃO
# expr=str(input('Digite a expressão: '))
# pilha=[]
# for simb in expr:
#     if simb =='(':
#         pilha.append('(')
#     elif simb == ')':
#         if len(pilha)>0:
#             pilha.pop()
#         else:
#             pilha.append(')')
#             break
# if len(pilha)==0:
#     print(f'Sua expressão está váida')
# else:
#     print(f'Sua expressão está inválida')