#FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFÍCIO, INDO DE 10 A 0, COM A PAUSA DE 1 SEGUNDO ENTRE ELES.

import time

for c in range(10,0,-1): #Se eu quiser utilizar o ZERO, coloco (10,-1,-1)
    print(c)
    time.sleep(1)
print('F O G O S')