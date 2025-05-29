#CORES NO TERMINAL
# \033[0;30;41m

# \033[4;33;44m

# \033[1;35;43m

# \033[30;42m

# \033[m

# \033[7;30m

print('\033[31mOlá mundo!')
print('\033[1;31;43mOlá mundo!\033[m')
print('\033[4;30;45mOlá, mundo!\033[m')
print('\033[7;33;44mOlá, mundo!\033[m')

a=3
b=5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))
print('Os valores são {} e {}{}{}'.format(a,'\033[34m',b,'\033[m'))