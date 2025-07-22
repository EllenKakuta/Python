'''
TRATAMENTO DE ERROS E EXCEÇÕES 

HÁ INÚMERAS EXCEÇÕES - EXCEPTION - Não é erro sintático, mas está tendo algum erro

Posso ter varios except com cada tipo de exceção, cada um com seu erro, com mensagem própria

try:
    operação
except TypeError:
    falhou
except ValueError:
    falhou
except OSError:
    falhou
else:
    deu certo
finally:
    certo/falha - vai acontecer se der falha ou não

'''

#PARTE PRÁTICA
try:
    a=int(input('Numerador: '))
    b=int(input('Denominador: '))
    r=a/b

except (ValueError,TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__cause__}')
else:    
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Obrigada!')