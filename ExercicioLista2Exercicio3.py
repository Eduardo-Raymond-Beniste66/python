peso = float(input('Peso:'))
multa = float(input('Multa'))
exesso = float(input('Exexxo'))
if peso > 50:
    exesso == peso - 50
    multa  == exesso  * 4
    
else:
    print(f'Multa: de R$ {multa :.2f}')
    print(f'Exesso:  {exesso :.2f}')
