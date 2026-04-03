def aumentar(num):
    mais = num + (num * 0.15)
    return mais

def diminuir(num):
    menos = num - (num * 0.10)
    return menos

def dobro(num):
    return num * 2

def metade(num):
    return num / 2

def moeda(num):
    return f'R${num:.2f}'.replace('.', ',')