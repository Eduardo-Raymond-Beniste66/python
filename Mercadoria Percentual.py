print('----Calculo de Percentual de Desconto----')

mercp=float(input('Insira o Preço da Mercadoria: ').replace(',','.'))
perc=float(input('Insira o percentual de Desconto: ').replace(',','.'))

valdesc=mercp*(perc/100)

print('O valor de desconto da mercadoria é R$ %.2f'%valdesc)

novoprec=mercp-valdesc
print('O valor da mercadoria com desconto é R$ %.2f'%novoprec)
