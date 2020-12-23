a = int(input('Ano'))
if a % 4 == 0  and (a % 100 != 0 or a % 4):
    print('bisexto')
else:
    print('Não é bisexto')
