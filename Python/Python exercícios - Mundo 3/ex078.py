#FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE-OS EM UMA LISTA
#NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA
valores=[]
for v in range(0,5):
    valores.append(int(input(f'Digite um valor para posição {v}: ')))
maior=max(valores)
menor=min(valores)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado é {maior} e está nas posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print(f'O menor valor digitado é {menor} e está nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')