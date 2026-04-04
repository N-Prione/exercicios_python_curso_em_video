def aumentar(num, taxa, sit=False):
    mais = num + (num * taxa/100)
    if sit == True:
        return moeda(mais)
    else:
        return mais
    
def diminuir(num, taxa, sit=False):
    menos = num - (num * taxa/100)
    if sit == True:
        return moeda(menos)
    else:
        return menos
    
def dobro(num, sit=False):
    if sit == True:
        return moeda(num * 2)
    else:
        return num * 2
    
def metade(num, sit=False):
    if sit == True:
        return moeda(num / 2)
    else:
        return num / 2
    
def moeda(num):
    return f'R${num:.2f}'.replace('.', ',')

def resumo(num, mais, menos):
    print(' --- RESUMO DOS VALORES ---'.center(45))
    print(f'Aumentar {mais}%: {aumentar(num, mais, True)}')
    print(f'Diminuir {menos}%: {diminuir(num, menos, True)}')
    print(f'Dobro do valor: {dobro(num, True)}')
    print(f'Metade do valor: {metade(num, True)}')