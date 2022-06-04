altura = float(input('Digite a altura da pessoa: ').replace(',','.'))

peso_Ideal1 = (72.2*altura) - 58
peso_Ideal2 = (62.1*altura) - 44.7

print(f'O peso ideal para homens é: {peso_Ideal1}')
print(f'O peso ideal para mulheres é: {peso_Ideal2}')