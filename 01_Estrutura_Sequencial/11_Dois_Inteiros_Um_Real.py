int1 = int(input('Digite um número inteiro: '))
int2 = int(input('Digite um número inteiro: '))
real = float(input('Digite um número real: ').replace(',','.'))

print(f'O produto dobro do primeiro com metade do segundo: {(int1*2)*(int2/2)}')
print(f'A soma do triplo do primeiro com o terceiro: {int1*3 + real}')
print(f'o terceiro elevado ao cubo {real**3}')