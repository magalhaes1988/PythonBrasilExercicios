salarioHora = float(input('Digite o valor da hora do seu salário: ').replace(',','.'))
horasTrabalhadas = float(input('Digite a quantidade de horas trabalhadas no mês: ').replace(',','.'))

totalSalario = salarioHora*horasTrabalhadas

print(f'Total do salário no mês é: {totalSalario}')