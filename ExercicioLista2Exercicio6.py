m = float(input('Metro:'))
if m % 54 == 0:
    latas = m / 54
else:
    latas = float(m / 54 + 1)
    valor = latas * 80
print(f'latas:{latas}')
print(f'total: {valor :.21}')
      
