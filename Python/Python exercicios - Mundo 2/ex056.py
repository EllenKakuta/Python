#DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA, MOSTRE:
#-A MÉDIA DE IDADE DO GRUPO
#-QUAL O NOME DO HOMEM MAIS VELHO
#-QUANTAS MULHERES TEM MENOS DE 20 ANOS

maior_idade=0
homem_mais_velho=''
idades=0
menores=0
for c in range(1,5):
    print('------- {}ª PESSOA ------'.format(c))
    nome=str(input('Nome: ')).title().strip()
    idade=int(input('Idade: '))
    idades+=idade
    sexo=str(input('Sexo [M/F]: ')).upper()
    if sexo=='F' and idade <20:
        menores+=1
    elif sexo=='M'and idade>maior_idade:
        maior_idade=idade
        homem_mais_velho=nome
if homem_mais_velho!='':
    print('O nome do homem mais velho é {}, ele tem {} anos'.format(homem_mais_velho,maior_idade))
media=idades/4
print('A média de idade do grupo é {:.1f} anos'.format(media))
print('{} mulheres tem menos de 20 anos.'.format(menores))