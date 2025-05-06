#PROGRMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME DE ACORDO COM SUA IDADE
#SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR
#SE É HORA DE SE ALISTAR
#SE JÁ PASSOU DO TEMPO DE ALISTAMENTO
#O PROGRAMA TAMBÉM DEVE MOSTRAR O TEMPO QUE FALTA OU PASSOU DO PRAZO
import datetime
nascimento = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - nascimento
# print(idade)
if idade < 18:
    print('Você tem {} anos, ainda falta(m) {} ano(s) para poder se alistar no serviço militar'.format(idade, (18-idade)))
elif idade == 18:
    print('Você tem {} anos, está na hora de se alistar no serviço militar'.format(idade))
else:
    print('Você tem {} anos, ultrapassou {} ano(s) da idade para o alistamento'.format(idade, (idade-18)))