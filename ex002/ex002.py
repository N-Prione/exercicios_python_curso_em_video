import moeda

valor = float(input('Digite um valor: R$ '))
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'Aumento de 15% de {moeda.moeda(valor)} é {moeda.moeda(moeda.aumentar(valor))}')
print(f'Diminuição de 10% de {moeda.moeda(valor)} é {moeda.moeda(moeda.diminuir(valor))}')