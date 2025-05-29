#FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUÁRIO. O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO


while True:
    multiplicador=1
    numero=int(input('Qual a tabuada desejada? '))
    if numero <0:
        print('Encerrando programa..')
        break
    while multiplicador<=10:
        resultado=numero*multiplicador     
        multiplicador+=1
        print (f'{numero} X {multiplicador-1} = {resultado}')   
print('FIM')
