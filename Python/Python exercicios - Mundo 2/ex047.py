#CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NÚMEROS PARES QUE ESTÃO NO INTERVALO ENTRE 1 E 50

for c in range(1,51):
    if c%2==0:
        print(c, end=' ') #END usado para que os números apareçam ao lado um do outro e não embaixo

for x in range(2,51,2): #Faz com que ocorram menos iterações- exige menos da máquina
    print(x, end=' ')