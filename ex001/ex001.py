import moeda

valor = float(input('Digite um valor: R$ '))
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'Aumento de 15% de {valor} é {moeda.aumentar(valor)}')
print(f'Diminuição de 10% de {valor} é {moeda.diminuir(valor)}')