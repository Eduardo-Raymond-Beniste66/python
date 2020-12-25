    minuto = int(input('Minuto:'))
    if minutos <= 200:
    preço = 0.2
    elif minuto <= 400:
    preço 0.18
    elif minuto <= 800:
    preço 0.15
    else:
        preço = 0.8
    print(f'R$ {preço * minuto:.2f}')
