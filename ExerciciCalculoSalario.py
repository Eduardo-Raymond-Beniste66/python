

print('----Calculo de Percentual de Aumento----')

sal=float(input('Insira o Salário Inicial: ').replace(',','.'))
perc=float(input('Insira o percentual de Aumento: ').replace(',','.'))

novosal=sal+(sal*(perc/100))
print('O Salário Reajustado é R$ %.2f'%novosal)
