from utilidades import dado
from utilidades import moeda

valor = dado.leiaDinheiro('Digite um valor: R$ ')
moeda.resumo(valor, 15, 10)