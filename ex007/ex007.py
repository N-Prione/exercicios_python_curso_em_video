class Churrasco:
    consumo_padrao = 0.400
    def __init__(self, qtd_pessoas, valor_carne):
        self.qtd_pessoas = qtd_pessoas
        self.valor_carne = valor_carne

    def calculo(self):
        total_carne = self.qtd_pessoas * 0.400
        valor_total = total_carne * self.valor_carne
        valor_pessoa = valor_total / self.qtd_pessoas
        return f''' ---------------------
-> Quantidade de carne: {total_carne:.3f} Kg
-> Valor total: R$ {valor_total:.2f}
-> Valor por pessoa: R$ {valor_pessoa:.2f}
---------------------'''

qtd_pessoas = int(input('Quantas pessoas vão para o churrasco? '))
valor_carne = float(input('Qual valor da carne? R$ ').replace(',', '.'))
churras = Churrasco(qtd_pessoas, valor_carne)
print(churras.calculo())