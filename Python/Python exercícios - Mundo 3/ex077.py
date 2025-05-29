#CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS(NÃO USAR ACENTOS)
#DEPOIS DISSO, VOCÊ DEVE MOSTRAR, PARA CADA PALAVRA, QUAIS SÃO SUAS VOGAIS
#(APRENDER, PROGRAMAR, LINGUAGEM, PYTHON, CURSO, GRATIS, ESTUDAR, PRATICAR, TRABALHAR, MERCADO, PROGRAMADOR, FUTURO)
palavras=('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for palavra in palavras:
    vogais=''
    for letra in palavra:
        if letra in 'AEIOU' :
            vogais+=letra
    print(f'As vogais da palavra {palavra} são {vogais}')


#CORREÇÃO VIA AULA
# for palavra in palavras:
#     print(f'\nNa palavra {palavra} temos', end=' ')
#     for letra in palavra:
#         if letra in 'AEIOU' :
#             print(letra,end=' ')
  