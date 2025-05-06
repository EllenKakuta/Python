#PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE
#ATÉ 9 ANOS: MIRIM
#ATÉ 14 ANOS: INFANTIL
#ATÉ 19 ANOS: JUNIOR
#ATÉ 20 ANOS: SÊNIOR
#ACIMA: MASTER

import datetime
print('CATEGORIA DO ATLETA DE ACORDO COM SUA IDADE')
nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = datetime.date.today().year - nascimento
if idade <= 9:
    print('Atleta possui {} anos - Categoria Mirim'.format(idade))
elif idade >9 and idade <=14:
    print('Atleta possui {} anos - Categoria Infantil'.format(idade))
elif idade > 14 and idade <=19:
    print('Atleta possui {} anos - Categoria Júnior'.format(idade))
elif idade == 20:
    print('Atleta possui {} anos - Categoria Sênior'.format(idade))
else:
    print('Atleta possui {} anos - Categoria Master'.format(idade))