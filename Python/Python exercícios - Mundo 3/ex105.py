#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO NOTAS() QUE PODE RECEBER VÁRIAS NOTAS DE ALUNOS E VAI RETORNAR UM DICIONÁRIO COM AS SEGUINTES INFORMAÇÕES:
# QUANTIDADE DE NOTAS
# A MAIOR NOTA
# A MENOR NOTA
# A MÉDIA DA TURMA
# A SITUAÇÃO (OPCIONAL)
#ADIONE TAMBÉM AS DOSCTRINGS DA FUNÇÃO

def notas(notas,sit=False):
    """
       Calcula estatísticas de notas escolares inseridas pelo usuário.

    Parâmetros:
    sit (bool): Valor opcional. Se True, adiciona uma análise da situação da média das notas.

    Retorna:
    dict: Um dicionário com as seguintes informações:
        - total: quantidade de notas inseridas
        - maior: a maior nota
        - menor: a menor nota
        - média: a média das notas
        - situação (opcional): situação da média (Boa, Razoável ou Ruim)
    """
    lista=[]
    total=0    
    while True:
        inicio=float(input('Informe a nota: '))             
        lista.append(inicio)                       
        total+=inicio               
        continua=str(input(f'Gostaria de acrescentar outra nota?[S/N] ')).upper().strip()
        if continua =='N':
            break    
    notas={
        'total':len(lista),
        'maior':max(lista),
        'menor':min(lista),
        'média':total/len(lista)
    }      
    if sit==True:
            if notas['média']>7:
                situacao='Boa'
            elif notas['média'] <5:
                situacao='Ruim'
            else:
                situacao='Razoável'
            notas['situação']=situacao    
    return notas
          
print(notas(notas))
help(notas)
