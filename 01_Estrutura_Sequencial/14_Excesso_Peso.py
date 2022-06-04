peso = float(input("Digite o total pescado: ").replace(',','.'))

if(peso>50):
    excesso = peso - 50
    multa = excesso*4

print(f'O peso excedido na pescaria foi: {excesso} Kg\nO valor da multa a ser paga é R$ {multa}')
