#Modulo de arrendondamento para cima biblioteca Math
from math import ceil

area = int(input('Entre com a área total a ser pintada: '))

litros = area/6

#Situação um somente galoes de 18 litros
latas_18 = ceil(litros/18)
preco_18 = latas_18*80

print(f'A quantidade total de latas de 18 litros, necessária é de {latas_18}\n\
com um custo de R$ {preco_18:.2f}')

#Situação dois galoes de 3,6 litros
latas_36 = ceil(litros/3.6)
preco_36 = latas_36*25

print(f'A quantidade total de latas de 3,6 litros, necessária é de {latas_36}\n\
com um custo de R$ {preco_36:.2f}')

litros_folga = area/6*1.1

latas_18m = ceil(litros_folga//18)
preco_18m = latas_18m*80
latas_36m = ceil((litros_folga - latas_18m*18)/3.6)
preco_36m = latas_36m*25

print(f'A quantidade de latas necessárias é de {latas_18m} de 18 litros e\n\
e de {latas_36m} de 3,6 litros com custo total de R$ {(preco_18m + preco_36m):.2f}')



