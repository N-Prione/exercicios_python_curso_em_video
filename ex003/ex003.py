import moeda

valor = float(input('Digite um valor: R$ '))
print(f'Aumento de 15% de {moeda.moeda(valor)} é {moeda.aumentar(valor, 15, True)}')
print(f'Diminuição de 10% de {moeda.moeda(valor)} é {moeda.diminuir(valor, 10, True)}')
print(f'Dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'Metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')