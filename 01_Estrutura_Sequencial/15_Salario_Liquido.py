salarioHora = float(input('Entre com o seu salário por hora: ').replace(',','.'))
horasTrabalhadas = int(input('Entre com as horas trabalhadas no mês: '))

salarioBruto = salarioHora*horasTrabalhadas
ir = salarioBruto*0.11
inss = salarioBruto*0.08
sindicato = salarioBruto*0.05
salarioLiquido = salarioBruto - ir -inss -sindicato

print(f'+ Salário Bruto: R$ {salarioBruto}\n\
- IR (11%): R$ {ir}\n\
- INSS (8%): R$ {inss}\n\
- Sindicato (5%): R$ {sindicato}\n\
= Salário Liquido: R$ {salarioLiquido}')

