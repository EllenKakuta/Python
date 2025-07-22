#CRIE UM CÓDIGO EM PYTHON QUE TESTE SE O SITE PUDIM ESTÁ ACESSÍVEL PELO COMPUTADOR USADO

from urllib import request

try:
    site = request.urlopen('http://www.pudim.com.br')
    print('Consegui acessar o site!')
    # print(site.read()) #PEga o conteudo HTML do site acessado
except:
    print('O site não está acessível no momento.')
