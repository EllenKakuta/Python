def aumentar(preco,porc,conversao=False):
    porcentagem=preco*(porc/100)
    total=preco+porcentagem
    if conversao==True:
        return moeda(total)
    return total

def diminuir(preco,porc,conversao=False):
    porcentagem=preco*(porc/100)
    total=preco-porcentagem
    if conversao==True:
        return moeda(total)
    else:
        return total

def dobro(preco,conversao=False):
    total=preco*2
    if conversao==True:
        return moeda(total)
    else:
        return total

def metade(preco,conversao=False):
    total=preco/2
    if conversao==True:
        return moeda(total)
    else:
        return total

def moeda(preco):
    return f'R$ {preco:>.2f}'.replace('.', ',')

def resumo(preco,aumento,reducao):
    print('-'*35)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-'*35)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco,True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco,aumento,True)}')
    print(f'{reducao}% de redução: \t{diminuir(preco,reducao,True)}')
    print('-'*35)

