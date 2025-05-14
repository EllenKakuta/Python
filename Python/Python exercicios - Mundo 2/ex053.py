#CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALINDROMO (A MESMA FRASE ESCRITA DE TRÁS PRA FRENTE) DESCONSIDERANDO OS ESPAÇOS
#EX: APOS A SOPA/ A SACADA DA CASA/ A TORRE DA DERROTA/ O LOBO AMA O BOLO/ ANOTARAM A DATA DA MARATONA

frase= str(input('Digite a frase a ser analisada: ')).strip().upper()
fraseSemEspaco= frase.replace(' ','')
# print(fraseSemEspaco)
inverso =''
for letra in fraseSemEspaco:
    inverso = letra+inverso
print('O inverso de {} é: {}'.format(fraseSemEspaco,inverso))
if fraseSemEspaco == inverso:
    print('A frase informada é um palíndromo')
else:
    print('A frase informada não é um palíndromo')


#outra forma de fazer o inverso
#inverso=fraseSemEspaco[::-1] - sem o laço de repetição
#OU
#for letra in range(len(fraseSemEspaco)-1,-1,-1)