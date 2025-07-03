#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ESCREVA(), QUE RECEBA UM TEXTO QUALQUER COMO PARÂMETRO E MOSTRE UMA MENSAGEM COM TAMANHO ADAPTÁVEL. Não precisa de input
#EX:
#escreva('Olá, Mundo!')
#SAÍDA
#-------------
# Olá, Mundo!
#-------------

def escreva(texto):
    t=len(texto)
    print('~'*t)
    print(texto)
    print('~'*t)

texto=str(input('Frase: '))
escreva(texto)


