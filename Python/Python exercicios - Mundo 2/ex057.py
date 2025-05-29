#FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE VALORES 'M' OU 'F'. CASO ESTEJA ERRADO, PEÇA DIGITAÇÃO NOVAMENTE ATÉ TER UM CORRETO.

sexo= str(input('Qual seu sexo? [M/F]: ')).strip().upper()[0]#para pegar a primeira letra
while sexo !='F'and sexo !='M' :
    sexo=str(input('Dados inválidos. Favor inserir novamente: ')).strip().upper()[0]   
print('Obrigada pela resposta!')