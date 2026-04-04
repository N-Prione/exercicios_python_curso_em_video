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