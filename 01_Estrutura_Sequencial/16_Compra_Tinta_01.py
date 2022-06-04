from math import ceil

area = int(input('Entre com a área total a ser pintada: '))

litros = area/3
latas = ceil(litros/18)
precoTotal = latas*80

print(f'A quantidade total de latas necessária é {latas} latas\n\
O preço total é de R$ {precoTotal}')