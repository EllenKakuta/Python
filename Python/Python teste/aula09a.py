frase = 'Curso em Vídeo Python'

print (frase)
print (frase[3])
print (frase[3:13])
print (frase[:13])
print (frase[13:])
print (frase[1:15:2])
print (frase[::2])
print (frase.count('o'))
print (len(frase))
print(frase.replace('Python', 'Android')) #substituii só nessa instancia
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])


frase2 = '  Curso em Vídeo Python  '
print(len(frase2))
print(len(frase2.strip())) #tira os espaços inicial e final
