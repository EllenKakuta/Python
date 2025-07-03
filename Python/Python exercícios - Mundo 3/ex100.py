#FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS E DUAS FUNÇÕES CHAMADAS SORTEIO() E SOMAPAR(). A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NÚMEROS E VAI COLOCÁ-LOS DENTRO DA LISTA E A SEGUNDA FUNÇÃO VAI MOSTRAR A SOMA ENTRE TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO ANTERIOR
import random
numeros=list()
def sorteio():
    for _ in range(0,6):
        num=random.randint(0,100)
        numeros.append(num)
    print(f'Números sorteados:{numeros}')

sorteio()

def somaPar():
    soma=0
    for n in numeros:
        if n % 2 == 0:
            soma+=n
    print(f'A soma entre os números pares sorteados é: {soma}')

somaPar()